from flask import Flask
app=Flask(__name__)
app.config["DEBUG"]=True

@app.route("/")
@app.route("/hello")

def hello_world():
	return 'welcome to our server'

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/interger/<int:value>")
def integer(value):
	print (value+1)
	return "correct"

@app.route("/float/<float:value>")
def float(value):
	print (value+1)
	return "correct"


@app.route("/path/<path:value>")	
def path_type(value):
	print(value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower()=="vrishank":
		return "Hello,{}".format(name),200
	else:
	    return "Not Found",478	





if __name__ == "__main__":
	app.run()