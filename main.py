from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "your_openai_api_key"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=100
        )
        return render_template("index.html", result=response.choices[0].text.strip())
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
