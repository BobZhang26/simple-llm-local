from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 从环境变量中获取API密钥
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")

        if not user_input:
            return render_template("index.html", error="No input provided.")

        # New API call using 'chat.completions'
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the latest GPT model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        result = response.choices[0].message["content"].strip()
        return render_template("index.html", result=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
client = OpenAI(
    api_key="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"
)

app = Flask(__name__)

# Set your OpenAI API key here


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")

        if not user_input:
            return render_template("index.html", error="No input provided.")

        # New API call using 'chat.completions'
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the latest GPT model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )

        # Extract the chatbot's response
        chatbot_response = response.choices[0].message.content
        return render_template(
            "index.html", user_input=user_input, chatbot_response=chatbot_response
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
