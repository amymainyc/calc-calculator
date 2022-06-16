from flask import Flask, render_template
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
  return render_template("base.html")

@app.route("/buttons")
def buttons():
	with open("templates/buttons.html", encoding="utf8") as f:
		return f.read()

@app.route("/calculus")
def calculus():
	with open("templates/calculus.html", encoding="utf8") as f:
		return f.read()

@app.route("/graphing")
def graphing():
	with open("templates/graphing.html", encoding="utf8") as f:
		return f.read()

@app.route("/other")
def other():
	with open("templates/other.html", encoding="utf8") as f:
		return f.read()

@app.route("/<function>/<input>")
def calculate(function, input):
	if function == "eval":
		return str(eval(input))
	input = input.split(",")
	for i in range(len(input)):
		try:
			input[i] = int(input[i])
		except:
			pass
	input.append(" ")
	f = globals()[function]
	if input[0] != "undefined":
		return str(f(input))
	else:
		return str(f())

if __name__ == "__main__":
  app.run(
		host='0.0.0.0',
		port=1000
	)