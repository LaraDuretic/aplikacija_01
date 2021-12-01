# Python Flask aplikacija

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/onama")
def onama():
    return render_template("o nama.html")

if __name__ == "__main__":
    app.run(use_reloader=True)
