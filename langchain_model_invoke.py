from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def main():
    model = init_chat_model("llama3-8b-8192", model_provider="groq")

    response1 = model.invoke("Hello")
    print(response1.content)
    print("\n")

    response2 = model.invoke([{"role": "user", "content": "Hello"}])
    print(response2.content)
    print("\n")

    response3 = model.invoke([HumanMessage("Hello")])
    print(response3.content)
    
    messages = [
        SystemMessage("You are a cringe know it all vibe coder"),
        HumanMessage("Hi code me a entire webapp for my protfolio"),
    ]

    for token in model.stream(messages):
        print(token.content, end="")

if __name__ == "__main__":
    main()