from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "abc"

@app.route("/")
def home():
    return "home page"

@app.errorhandler(404)
def page_404(error):
    print(error)
    return render_template("404.html")
