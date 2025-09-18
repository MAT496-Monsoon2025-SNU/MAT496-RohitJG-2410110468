from dotenv import load_dotenv
import cv2
load_dotenv(override=True)

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

@tool
def open_camera():
    "Opens your camera and takes a picture."
    print("Opening camera...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"{a}.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()
    return f"Picture taken and saved as {a}.jpg"

tools = [open_camera]

llm = llm.bind_tools(tools)

messages = [
    SystemMessage("You are an AI assistant that can use tools to help the user."),
    HumanMessage("Take a photo of me.")
]
response = llm.invoke(messages)
print(response.content)
print(response.tool_calls)

for t in response.tool_calls:
    print(t)
    if t['name'] == 'open_camera':
        tool_response = open_camera()
        print(f"Tool {t['name']} response: {tool_response}")