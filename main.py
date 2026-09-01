from core.graph import build_graph
from langchain_core.messages import HumanMessage

def main():
    print("[*] Initializing core...")
    app = build_graph()
    
    user_input = "You are in test mode. Introduce yourself briefly as my personal system assistant."
    print(f"\nUser: {user_input}")
    
    inputs = {"messages": [HumanMessage(content=user_input)]}
    result = app.invoke(inputs)
    
    ai_response = result["messages"][-1].content
    print(f"\nAssistant: {ai_response}")

if __name__ == "__main__":
    main()