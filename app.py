from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/keskiarvo")
def keskiarvo():
     return render_template("keskiarvo.html")

@app.route("/tarkkaosuus")
def tarkkaosuus():
     return render_template("tarkkaosuus.html") 
