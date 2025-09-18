from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from googlesearch import search

load_dotenv()

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

@tool
def search_google(query: str) -> str:
    "Searches the web using google search and returns the top result."
    return search(query)

tools = [search_google]
llm = llm.bind_tools(tools)

def main():
    messages = [
        SystemMessage("You are an AI assistant that can use tools to help the user search the web and get realtime data."),
        HumanMessage("What is the current weather in delhi?")
    ]
    response = llm.invoke(messages)
    print(response.content)
    print(response.tool_calls)

    for t in response.tool_calls:
        print(t)
        if t['name'] == 'search_google':
            tool_response = search_google(t['arguments']['query'])
            print(f"Tool {t['name']} response: {tool_response}")
