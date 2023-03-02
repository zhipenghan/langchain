# flake8: noqa
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question. The question may contains the answer format requirment. Output result in asked format.
"""

SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""


##

# Sample:
# Question: Are both the directors of Jaws and Casino Royale from the same country?
# Thought: I should look up who the directors are
# Action: Search
# Action Input: director of Jaws
# Observation: The director of Jaws is Steven Spielberg.
# Thought: I should look up director of Casino Royale
# Action: Search
# Action Input: director of Casino Royale
# Observation: The director of Casino Royale is Martin Campbell.
# Thought: I should look up country of Steven Spielberg and Martin Cmpbell.
# Action: Search
# Action Input: Where is Steven Spielberg from?
# Observation: The United States.
# Thought: I should look up country of Martin Cmpbell.
# Action: Search
# Action Input: Where is Martin Campbell from?
# Observation: New Zealand.
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question


