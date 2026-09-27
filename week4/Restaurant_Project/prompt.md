<!-- I am building a restaurant order management ai agent system using langGraph.

I will explain you very clearly what i want and what is the architecture. i will also explain you the nodes the state and the edges.
In the end i will give you test cases to simulate and to tell me whether they pass or not.

The rough plan is:
There will be a user. when the code runs the user will give an order. this will be taken as an input which i will type
This order should go to the llm. The order as of now should contain dish and the required quantity.
for simplicity purpose for now we will limit the ordert to one particular dish and whatever quantity the user wants.
the llm will have to exrtact the order name and the quasntuty from the user input.
if the user input is unrelated to food ordering, the llm should not process that and tell the user the same thing that is ian ai agaent
oof food ordering and not a generla purpose llm.

Once the llm has order dish and quantity
it will send that to a node caLLED order_confirm
The task of this order conform is to look at the menu (i will tell ypu the menu later in this prompt).
The\n this node will decide one of 3 case
the order is available 
the order is partially available means quantity is not suficient
the order is not available at all (dish being not i the menu or 0 quantity available)
it will put this in the status of the state (I will tell u the exact content of the langgraph state as well)

Once the llm recieved this
if the status is confiormed (full available) it should call another node called cook.
if the staus is partail or not available it should again prompty the user to decide
the user can either place a new order or can cionform if he wants to go ahead with the3 partial order

This order reties will be limited to 3 attempts menaing if after 3 attempt the user is not saidfied the system will come the the END node

Now wqhen the cook node is called
 there can be  2 casea
 eithet eh cook is done then the stasus will beREady
 and if the cook faikls( we can use a prob function). give 40% chanes of fail and 60 % chance of success

 if the cook fails there shgould be 1 more attempt allowed for cook to suceed. if the cook fails even after these
 then the llm should issue a aplogy to the user and come to END state

 if the cpook suuceeds, the status will be REAADY
 and the next node will be called which is serve
 simialr to cook this also has 2 cases
 servre pass or serve fail
 this also has 2 retry attempt
 if the serve fails 2 times then the llm should issue a aplogy to the user and come to END state

 if the serve suceeds the status should bceomc ocmplete the llm should uissue a message to the user saying your oder is complete
 if serve fails then cook should becalled one more time to retruy.
 Note that if cok has exhausted its retrey attempts then it should not cook again and llm should issue an apology and come to end state


 Now the state of lagragph

 there shoiuld be a annotated message be llm and user

 there should be order details
 dish name as str
 required quantuty as int
 available quantity as string
 order_conform will write the available quantuty by readibng the menu
 the llm should get to know the order confrm status by reading the state 
 if a dish is not avilabel in the mnu then orderconform should write 0 as avail qwuantuty

 then there should be status
 each node will update the status as specifed in the above rules
 then order retry attemps which are 3
 cook retry attemnpts which are 2
 serve retry attempts which are 2
 each time a filure haappend and a node is retrying it should diecreent the couner
 if any retry counter becomes 0 it means it is over. llm shoukd ubnderattnd whether it has to give a retry or issue apology by reading this vcounter
 in the end thre shoul be final; result whehter the orede was completed or not.




 Wreite the code and ask if there are any open questions from your side then ask
 i will give you some test scenaiors to test later on
 
 TC1
 a user aska unrealted question
 then he palces a order which is partial
 then he rejects the partial and wants to order again
 again he ordes a dish which is not avilabl
 expected. END due to order retry

 TC2
 user places a order which can be availeble
 cook makes it fails once
 cooks again cucess
 serve fails once
 cook retries success
 serve does success
 overall success

 TC3
 user orders partal
 doesn not want partial 
 orders again fuylly available
 cooks kakes it fails
 makes again success
 serve fails
 cook retries success
 serve fails again
 cook does not retry ue to cook retru exhaist
 overall FAIl -->




I am building a Restaurant Order Management AI Agent System using LangGraph.

I will explain clearly what I want, including the architecture, nodes, state, and edges. At the end, I will provide some test cases to simulate and verify whether the system passes them or not.

Rough Plan

There will be a User. When the program runs, the user will provide an order as text input.

For now, the order will contain only:

Dish name
Required quantity

For simplicity, we will support only one particular dish per order, with whatever quantity the user requests.

The user input will first go to the LLM.

The LLM will extract:

Dish name
Required quantity

If the user input is unrelated to food ordering, the LLM should not process it. Instead, it should tell the user that this is an AI Agent specifically designed for food ordering, not a general-purpose LLM.

Once the LLM has extracted the dish and quantity, it will send the information to a node called order_confirm.

Order Confirm Node

The order_confirm node will check the menu, which I will provide later.

It will determine one of three cases:

Available — The requested quantity is fully available.
Partially Available — The dish is available, but the available quantity is less than the requested quantity.
Not Available — The dish is not present in the menu or its available quantity is 0.

The order_confirm node will write the available quantity and the order status into the LangGraph state.

The LLM will then read the order confirmation status from the state.

If the status is confirmed/full available, the flow should proceed to the cook node.

If the status is partial or not available, the system should ask the user what they want to do.

The user can either:

Place a new order, or
Confirm that they want to proceed with the partial order.

The order retry limit will be 3 attempts. If the user is still not satisfied after 3 attempts, the system should go to the END state.

Cook Node

Once the cook node is called, there will be two possible outcomes:

Success → Status becomes READY
Failure → A retry should be attempted

For simulation, the cook operation should have:

40% probability of failure
60% probability of success

The cook will have a maximum of 2 attempts.

If cooking fails on the first attempt, one more attempt should be allowed.

If cooking fails again and the retry counter is exhausted, the LLM should issue an apology to the user and the system should go to the END state.

If cooking succeeds, the status becomes READY, and the next node should be serve.

Serve Node

The serve node will also have two possible outcomes:

Success → Status becomes COMPLETE
Failure → Retry flow

The serve operation will also have a maximum of 2 attempts.

If serving succeeds, the status becomes COMPLETE, and the LLM should tell the user that their order has been completed successfully.

If serving fails, the system should call the cook node again so that the order can be retried.

However, if the cook retry attempts have already been exhausted, the system must not call cook again. Instead, the LLM should issue an apology to the user and the system should go to the END state.

LangGraph State

The LangGraph state should contain:

Annotated messages between the LLM and User
Order details
dish_name: str
required_quantity: int
available_quantity: str
status

The order_confirm node will determine available_quantity by reading the menu.

If a dish is not available in the menu, order_confirm should write:

available_quantity = 0

The LLM should determine what to do next by reading the order confirmation status from the state.

Each node should update the status according to the rules described above.

The state should also contain retry counters:

order_retry_attempts = 3
cook_retry_attempts = 2
serve_retry_attempts = 2

Whenever a failure occurs and a retry is performed, the corresponding counter should be decremented.

If any retry counter becomes 0, it means that the corresponding retry attempts have been exhausted.

The LLM should understand whether it can retry or whether it needs to issue an apology and terminate the workflow by reading these counters from the state.

Finally, the state should contain a final result indicating whether the order was successfully completed or not.

Test Cases
TC1
User asks an unrelated question.
User then places an order that is partially available.
User rejects the partial order and wants to place a new order.
User orders a dish that is not available.
The system should reach END because the order retry limit has been exhausted.

Expected Result: FAIL / END due to order retry exhaustion

TC2
User places an order that is fully available.
Cooking fails once.
Cooking succeeds on the second attempt.
Serving fails once.
Cooking is retried and succeeds.
Serving succeeds.
Overall order should be completed successfully.

Expected Result: SUCCESS / COMPLETE

TC3
User orders a partially available item.
User does not want the partial order.
User places another order that is fully available.
Cooking fails once.
Cooking succeeds on the second attempt.
Serving fails.
Cooking is retried and succeeds.
Serving fails again.
Cooking should not be retried because the cook retry attempts are exhausted.
The LLM should issue an apology.
The system should reach END.

Expected Result: FAIL / END due to cook retry exhaustion

Task

Please write the complete LangGraph code for this architecture, including the state, nodes, edges, conditional edges, retry logic, LLM interaction, and user interaction.

Before finalizing the implementation, if there are any open questions or ambiguities in the architecture, ask me about them first. I will provide the answers and then give you the test scenarios to simulate.