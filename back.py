from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

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
