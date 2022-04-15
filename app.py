from flask import Flask, render_template, url_for, flash, redirect


app = Flask(__name__, template_folder='templates')

@app.route("/")

@app.route("/home")
def index():
    return render_template(r"index.html")