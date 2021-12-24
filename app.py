from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return ("Hello, this code was updated locally and pushed to Azure DevOps Repo!" ,
             "So nice that you finally saw my web application.", 
             "This is my first try to do so.", "Hope you like it.Thanks!!")
