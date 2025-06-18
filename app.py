from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Local database load karo
with open("database.json") as f:
    data = json.load(f)

# Matching function
def find_local_response(query):
    query = query.lower()
    for key in data:
        if key in query:
            return data[key]
    return "Sorry, I don't understand that yet."

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Chatbot response
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    response = find_local_response(user_input)
    return jsonify({"reply": response})

# Run server
if __name__ == "__main__":
    app.run(debug=True)


