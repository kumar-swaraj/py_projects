from dataclasses import dataclass
from typing import cast

from textblob import TextBlob


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(text: str, *, sensitivity: float) -> Mood:
    polarity = TextBlob(text).sentiment.polarity  # type: ignore
    polarity = cast(float, polarity)

    friendly_threshold = sensitivity
    hostile_threshold = -sensitivity

    if polarity >= friendly_threshold:
        return Mood("😊", polarity)
    elif polarity <= hostile_threshold:
        return Mood("😠", polarity)
    else:
        return Mood("😑", polarity)


def run_bot() -> None:
    print("Bot: Enter some text and I will perform a sentiment analysis on it.")
    while True:
        user_input = input("You: ")
        mood = get_mood(user_input, sensitivity=0.3)
        print(f"Bot: {mood.emoji} {mood.sentiment}")

        if user_input == "exit":
            break


if __name__ == "__main__":
    run_bot()
