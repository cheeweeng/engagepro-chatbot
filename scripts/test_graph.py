from langchain_core.messages import HumanMessage

from graph.workflow import graph

response = graph.invoke(
    {
        "messages": [
            HumanMessage(content="What is artificial intelligence?")
        ]
    }
)

print(response["messages"][-1].content)