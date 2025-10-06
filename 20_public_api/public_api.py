from datetime import datetime
from random import choice, randint

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    """This is homepage of api."""

    phrases = [
        "Welcome to this page!",
        "You are looking good today!",
        "The weather is great!",
    ]
    return {
        "phrase": choice(phrases),
        "datetime": str(datetime.now()).split(sep=".")[0],
    }


@app.route("/api/random")  # /api/random?number=10000&text=helloworld
def random():
    """The random endpoint of our api."""

    # Define some queries for our api endpoint
    number_input = request.args.get("number", type=int)
    text_input = request.args.get("text", type=str, default="default_text")

    # Check that the number is of the correct type before doing anything
    if isinstance(number_input, int):
        return {
            "input": number_input,
            "random": randint(0, number_input),
            "text": text_input,
            "date": datetime.now(),
        }
    else:
        return {"Error": "Please only enter numbers."}


if __name__ == "__main__":
    app.run()
