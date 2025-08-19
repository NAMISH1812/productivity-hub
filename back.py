from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_msg}]
    )
    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

