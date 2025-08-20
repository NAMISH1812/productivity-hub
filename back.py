from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)  # 👈 add this immediately after creating the app

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_msg}]
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
