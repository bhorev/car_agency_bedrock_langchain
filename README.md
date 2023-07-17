# Bedrock LLM with LangChain Agent with a tool to invoke a function and a tool to lookup in a SQL database

This simplified example demonstrates the use of Amazon Bedrock LLM together with LangChain to answer questions about car prices.

There are two use-cases:

- Answer questions about car prices based on a function
- Search for an available car in a used-cars SQL database

For this purpose, we use LangChain Agent and Tools.

There are questions which the LLM cannot answer by itself. For example, get curernt events (news, weather), perform a complex math calculation, lookup data in a database. But we can create tools to do all of that - web search, function execution, database lookup. Langchain has readily available tools and we can also create our own custom tools.
Beyond the tools themselves, we want to use the LLM in order to decide when to invoke an appropriate tool. With agents, the LLM is capable of deciding in a zero-shot prompt scenario which tool to invoke, in order to obtain context which is then utilized to construct the final answer.

Amazon Bedrock model: anthropic.claude-v1

Notebooks:
- *cars_challenge.ipynb* - Shows the first use-case as an example and leaves the second one as a challenge for the reader
- *cars_answer.ipynb* - Shows both use-cases
