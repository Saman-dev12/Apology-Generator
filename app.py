from flask import Flask, render_template, request
from apologyGenerator import generate_apology

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generateApology():
    apologyType = request.form['apology']
    apology = generate_apology(apologyType)
    return render_template("apology.html", apology=apology)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
