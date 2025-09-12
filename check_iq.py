from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

def generate_iq_question(model):
    messages = [
        SystemMessage("You are an IQ test creator. Generate a challenging but fair IQ question that tests logical reasoning, pattern recognition, or mathematical thinking. Provide only the question, not the answer."),
        HumanMessage("Create an IQ question that would be appropriate for testing intelligence.")
    ]
    
    response = model.invoke(messages)
    return response.content

def solve_iq_question(model, question):
    messages = [
        SystemMessage("You are taking an IQ test. Think step by step and provide your reasoning before giving your final answer."),
        HumanMessage(f"Solve this IQ question: {question}")
    ]
    
    response = model.invoke(messages)
    return response.content

def main():
    question_generator = init_chat_model("gpt-4o-mini", model_provider="openai")
    question_solver = init_chat_model("llama3-8b-8192", model_provider="groq")
    
    print("generating iq test")
    iq_question = generate_iq_question(question_generator)
    print(f"Generated Question: {iq_question}\n")
    
    print("Solving with Llama3-8b...")
    solution = solve_iq_question(question_solver, iq_question)
    print(f"Solution: {solution}\n")
    
    correct_answer_messages = [
        SystemMessage("You are an IQ test creator. Provide the correct answer and explanation for the question you created."),
        HumanMessage(f"What is the correct answer to this question you created: {iq_question}")
    ]
    
    correct_answer = question_generator.invoke(correct_answer_messages)
    print(f"Correct Answer: {correct_answer.content}\n")
    
    print("Compare the solver's answer with the correct answer to evaluate performance!")

if __name__ == "__main__":
    main()
