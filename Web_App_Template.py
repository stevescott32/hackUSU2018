from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Home Page!</h1>" 

@app.route("/AnxietyExam")
def E_Exam():
	return render_template('test.html')
	

@app.route("/DepressionExam")
def D_Exam():
	return "<h1>This is the about page!</h1>" 

@app.route("/Results_A")
def results_1():
	return "<h1>This is the about page!</h1>" 

@app.route("/Results_D")
def results_2():
	return "<h1>This is the about page!</h1>" 			