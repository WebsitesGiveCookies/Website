from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "abc"

@app.route("/")
def home():
    return render_template("index.html")

  
