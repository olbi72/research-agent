from agent import agent


def extract_final_ai_message(response) -> str:
    messages = response.get("messages", [])
    for message in reversed(messages):
        if getattr(message, "__class__", None).__name__ == "AIMessage" and getattr(message, "content", ""):
            return message.content
    return "No final response generated."


def main():
    print("Research Agent CLI")
    print("Type your question, or type 'exit' to quit.")

    config = {"configurable": {"thread_id": "interactive-session-1"}}

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = agent.invoke(
                {
                    "messages": [
                        {"role": "user", "content": user_input}
                    ]
                },
                config=config,
            )

            final_answer = extract_final_ai_message(response)
            print(f"\nAgent:\n{final_answer}")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
