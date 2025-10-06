import sys
from difflib import get_close_matches


def get_best_match(user_question: str, questions: dict[str, str]) -> str | None:
    """Compares the user message similarity to the ones in the dictionary."""
    matches = get_close_matches(user_question, questions.keys(), n=1, cutoff=0.6)

    return matches[0] if matches else None


def chatbot(knowledge: dict[str, str]):
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            sys.exit()

        best_match = get_best_match(user_input, knowledge)

        answer = knowledge.get(best_match) if best_match else None
        if answer:
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't understand... Could you try rephrasing that?")


def main() -> None:
    brain = {
        "hello": "Hey there!",
        "how are you?": "I am good, thanks!",
        "do you know what the time is?": "Not at all!",
        "what time is it?": "No clue!",
        "what can you do?": "I can answer questions!",
        "ok": "Great.",
    }

    chatbot(knowledge=brain)


if __name__ == "__main__":
    main()
