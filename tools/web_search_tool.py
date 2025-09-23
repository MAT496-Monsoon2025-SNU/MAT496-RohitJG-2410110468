from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from googlesearch.googlesearch import GoogleSearch
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search"
    )
]

def main():
    query = input("Please enter your search query: ")
    self_ask_with_search = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True)
    self_ask_with_search.run(quert)



    # for t in response.tool_calls:
    #     print(t)
    #     if t['name'] == 'search_google':
    #         tool_response = search_google(t['arguments']['query'])
    #         print(f"Tool {t['name']} response: {tool_response}")

if __name__ == "__main__":
    main()
