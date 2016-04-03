from flask import Flask,render_template,redirect,request
from hashids import Hashids
from functions import *

cypher = Hashids(salt = "WP-A.co")
app = Flask(__name__)

def NewViewReturn(urlprocessar, customaadd):
	return(render_template("added.html",FullURL = DefaultFunctions.URLProcessing(urlprocessar, customaadd)))

@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("index.html")

@app.route("/new/", methods=['GET', 'POST'])
def newurl():
	return render_template("new.html")

@app.route("/about/", methods=['GET', 'POST'])
def about():
	return render_template("about.html")

@app.route("/login/", methods=['GET', 'POST'])
def loginPage():
	return render_template("login.html")


@app.route("/add/", methods=['GET', 'POST'])
def login():
	global URLadd, CustomURL
	URLadd = request.args.get('url')
	CustomURL = request.args.get('customshort')
	return(NewViewReturn(URLadd, CustomURL))

@app.route("/api/", methods=['GET', 'POST'])
def apiURL():
	global URLadd, CustomURL
	URLadd = request.args.get('url')
	CustomURL = request.args.get('customshort')
	ReturnMethod = request.args.get('method')
	try:
		if ReturnMethod == "json":
			ExitingString = "{ 'url' : " + processaURL(URLadd, CustomURL) + "}"
			return(ExitingString)
		elif ReturnMethod == "http":
			return(processaURL(URLadd, CustomURL))
		elif ReturnMethod == "":
			return("Error: No Method Defined!")
	except ValueError:
		return("Error: No Method Defined!")

@app.route("/u/<urlcode>", methods=['GET', 'POST'])
def CheckURL(urlcode):
	RedirectTo = DefaultFunctions.AccessURL(urlcode)
	return render_template("render-url.html",RedirectTo = RedirectTo)

if __name__ == "__main__":
       app.run(port=BSPort, debug=DBGState, host=BSHost)
