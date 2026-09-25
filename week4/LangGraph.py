# from typing import TypedDict
# from langgraph.graph import END, StateGraph


# class State(TypedDict):
#     number: int


# def double(state: State) -> dict:
#     boardnum = state["number"]
#     newnum = boardnum * 2

#     print("in double")
#     print(newnum)

#     return {"number": newnum}


# def finish(state: State) -> dict:
#     boardnum = state["number"]

#     print("in finish")
#     print(boardnum)

#     return {"number": boardnum}


# def decision(state: State) -> str:
#     if state["number"] < 100:
#         return "double"
#     else:
#         return "finish"


# builder = StateGraph(State)

# builder.add_node("double", double)
# builder.add_node("finish", finish)

# # Entry point
# builder.set_entry_point("double")

# builder.add_conditional_edges(
#     "double",
#     decision,
#     {
#         "double": "double",
#         "finish": "finish",
#     },
# )

# builder.add_edge("finish", END)

# graph = builder.compile()


# if __name__ == "__main__":
#     result = graph.invoke({"number": 3, "log": ""})


from typing import TypedDict
from langgraph.graph import END, StateGraph


class State(TypedDict):
    number: int


def double(state: State) -> dict:
    boardnum = state["number"]
    newnum = boardnum * 2

    print("in double")
    print(newnum)

    return {"number": newnum}


def finish(state: State) -> dict:
    boardnum = state["number"]

    print("in finish")
    print(boardnum)

    return {"number": boardnum}


def decision(state: State) -> str:
    if state["number"] < 100:
        return "double"
    else:
        return "finish"


# Create graph
builder = StateGraph(State)

builder.add_node("double", double)
builder.add_node("finish", finish)

# Entry point
builder.set_entry_point("double")

# Conditional edges
builder.add_conditional_edges(
    "double",
    decision,
    {
        "double": "double",
        "finish": "finish",
    },
)

# Finish the graph
builder.add_edge("finish", END)

# Compile graph
graph = builder.compile()


if __name__ == "__main__":

    # User input
    number = int(input("Enter a number: "))

    # Run graph
    result = graph.invoke({
        "number": number
    })

    print("Final Result:", result["number"])