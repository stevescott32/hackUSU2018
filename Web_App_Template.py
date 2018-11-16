from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Home Page!</h1>" 

@app.route("/about")
def about_func():
	return "<h1>This is the about page!</h1>" 