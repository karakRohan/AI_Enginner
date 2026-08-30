# import os
# from pathlib import Path
# from time import sleep
# from dotenv import load_dotenv
# from groq import Groq
# import re

# load_dotenv()
# my_api_key=os.getenv("GROQ_API_KEY")

# if not my_api_key:
#     raise ValueError("API key kaha hai bhai")

# client=Groq(api_key=my_api_key)
# # model="llama-3.3-70b-versatile"
# model="openai/gpt-oss-20b",


# def get_product_price(product):
#     if product == 'iPhone 17':
#         return 1000
#     elif product == "iPhone 15":
#         return 500
#     else:
#         return 0
    
# def calculator(expression):
#     try:
#         return eval(expression)
#     except:
#         return "calc error!"

# tools = {
#     "get_product_price": get_product_price,
#     "calculator": calculator
# }
# system_prompt = """
# You are a shopping assistant.

# You have these tools:

# get_product_price(product)
# calculator(expression)
# IMPORTANT:
# Call tools exactly like these examples:

# Action: get_product_price("iPhone 17")
# Action: calculator("5000 - 1000")

# Never write:
# get_product_price(product="iPhone 17")

# Never write:
# calculator(expression="5000 - 1000")
# Follow these rules:

# 1. Decide what you need to do next.
# 2. Call ONLY ONE tool at a time.
# 3. After writing an Action, STOP immediately.
# 4. Never guess or invent a tool result.
# 5. Wait until you receive an Observation.
# 6. Then decide your next action.
# 7. When the task is complete, give the Final Answer.

# Format:

# Thought: what you need to do
# Action: tool_name(argument)

# When finished:

# Final Answer: your answer
# """

# def run_agent(question):

#     messages = [
#         {
#             "role": "system",
#             "content": system_prompt
#         },
#         {
#             "role": "user",
#             "content": question
#         }
#     ]

#     for step in range(5):

#         print("\n------------------")
#         print("STEP", step + 1)
#         print("------------------")

#         response = client.chat.completions.create(
#             # model="llama-3.3-70b-versatile",
#             model="openai/gpt-oss-20b",
#             messages=messages,
#             temperature=0
#         )

#         answer = response.choices[0].message.content

#         print(answer)

#         # Agent has finished
#         if "Final Answer:" in answer:
#             break


#         # Find the Action
#         match = re.search(
#             r"Action:\s*(\w+)\((.*?)\)",
#             answer
#         )


#         if match:

#             tool_name = match.group(1)

#             tool_input = match.group(2)

#             tool_input = tool_input.strip()

#             tool_input = tool_input.strip('"')


#             # Run the tool
#             if tool_name in tools:

#                 tool = tools[tool_name]

#                 observation = tool(tool_input)

#             else:

#                 observation = "Tool not found"


#             print(
#                 "Observation:",
#                 observation
#             )


#             # Add LLM response to memory
#             messages.append({
#                 "role": "assistant",
#                 "content": answer
#             })


#             # Give tool result back to LLM
#             messages.append({
#                 "role": "user",
#                 "content":
#                     "Observation: "
#                     + str(observation)
#             })
#             sleep(5)



# prompt="""
# I have 5000 rupees. What is the price of an iphone 17?
# and how much money will I have left?
# """
# run_agent(prompt)




import os
import json

from dotenv import load_dotenv
from groq import Groq


# =========================================
# 1. LOAD ENVIRONMENT
# =========================================

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")


# =========================================
# 2. GROQ CLIENT
# =========================================

client = Groq(api_key=my_api_key)


# =========================================
# 3. MODEL
# =========================================

model = "openai/gpt-oss-20b"


# =========================================
# 4. TOOLS / FUNCTIONS
# =========================================

def get_product_price(product):

    if product == "iPhone 17":
        return 1000

    elif product == "iPhone 15":
        return 500

    else:
        return 0


def calculator(expression):

    try:
        return eval(expression)

    except Exception:
        return "calc error!"


# =========================================
# 5. TOOL SCHEMAS
# =========================================

get_product_price_tool = {
    "type": "function",
    "function": {
        "name": "get_product_price",
        "description": "Get the price of a product.",
        "parameters": {
            "type": "object",
            "properties": {
                "product": {
                    "type": "string",
                    "description": "Name of the product"
                }
            },
            "required": ["product"]
        }
    }
}


calculator_tool = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Calculate a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression to calculate"
                }
            },
            "required": ["expression"]
        }
    }
}


# =========================================
# 6. TOOLS LIST
# =========================================

tools = [
    get_product_price_tool,
    calculator_tool
]


# =========================================
# 7. TOOL EXECUTOR
# =========================================

def execute_tool(tool_name, arguments):

    if tool_name == "get_product_price":

        product = arguments["product"]

        return get_product_price(product)


    elif tool_name == "calculator":

        expression = arguments["expression"]

        return calculator(expression)


    else:

        return "Tool not found"


# =========================================
# 8. RUN AGENT
# =========================================

def run_agent(question):

    messages = [

        {
            "role": "system",
            "content": """
You are a shopping assistant.

You have access to two tools:

1. get_product_price
2. calculator

Use the tools whenever necessary.

For example:

If the user asks for the price of iPhone 17,
use get_product_price.

If the user asks how much money is left,
use calculator.

Use only one tool at a time.

After receiving a tool result, decide what to do next.

When everything is complete, provide a clear final answer.
"""
        },

        {
            "role": "user",
            "content": question
        }

    ]


    # =========================================
    # AGENT LOOP
    # =========================================

    for step in range(5):

        print("\n------------------")
        print("STEP", step + 1)
        print("------------------")


        # =====================================
        # CALL MODEL
        # =====================================

        response = client.chat.completions.create(

            model=model,

            messages=messages,

            tools=tools,

            tool_choice="auto",

            parallel_tool_calls=False,

            temperature=0

        )


        message = response.choices[0].message


        # =====================================
        # CHECK TOOL CALL
        # =====================================

        if message.tool_calls:

            # Add assistant message to conversation
            messages.append(
                message.model_dump(exclude_none=True)
            )


            # Only one tool because
            # parallel_tool_calls=False

            tool_call = message.tool_calls[0]


            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            print("Tool:", tool_name)

            print("Arguments:", arguments)


            # =================================
            # EXECUTE TOOL
            # =================================

            observation = execute_tool(
                tool_name,
                arguments
            )


            print(
                "Observation:",
                observation
            )


            # =================================
            # SEND TOOL RESULT BACK TO MODEL
            # =================================

            messages.append(
                {
                    "role": "tool",

                    "tool_call_id": tool_call.id,

                    "name": tool_name,

                    "content": str(observation)
                }
            )


        else:

            # =================================
            # FINAL ANSWER
            # =================================

            print("\nFinal Answer:")

            print(message.content)

            break


# =========================================
# 9. USER PROMPT
# =========================================

prompt = """
I have 5000 rupees.

What is the price of an iPhone 17?

And how much money will I have left?
"""


# =========================================
# 10. START AGENT
# =========================================

run_agent(prompt)