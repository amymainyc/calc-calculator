from flask import Flask, render_template
import random
from functions.buttons import *
from functions.calculus import *
from functions.graph import *
from functions.other import *

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='static'
)
app.config["SECRET_KEY"] = "OIJGR03I4JGFJN0Q3J0GI"

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/eval/<e>")
def evaluate(e):
	return str(eval(e))

if __name__ == "__main__":
  app.run(
		host='0.0.0.0',
		port=2461
	)