from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Home Page!</h1>" 

@app.route("/about")
def about_func():
	return "<h1>This is the about page!</h1>" 

@app.route("/anxiety_assessment")
def anxiety_assessment():
    return "<h1>Anxiety assessment page</h1>"

@app.route("/anxiety_assessment/results")
def anxiety_assessment_results():
    return "<h1>Anxiety assessment results page</h1>"

@app.route("/depression_assessment")
def depression_assessment():
    return "<h1>Depression assessment page</h1>"

@app.route("/depression_assessment/results")
def depression_assessment_results():
    return "<h1>Depression assessment results page</h1>"

