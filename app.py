from flask import Flask, request, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why do Java developers wear glasses? Because they can't C#.",
    "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
    "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
    "There are only 10 types of people in the world: those who understand binary and those who don't.",
]


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Joke API!", "endpoints": {"/joke": "GET a random joke", "/joke": "POST to submit a new joke"}})


@app.route("/joke", methods=["GET"])
def get_joke():
    return jsonify({"joke": random.choice(jokes)})


@app.route("/joke", methods=["POST"])
def submit_joke():
    data = request.get_json()
    if not data or "joke" not in data:
        return jsonify({"error": "Please provide a joke in JSON format: {\"joke\": \"your joke\"}"}), 400

    jokes.append(data["joke"])
    return jsonify({"message": "Joke added successfully!", "total_jokes": len(jokes)}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
