from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def hello():
	return render_template('HomePage.HTML')

@app.route("/anxiety_assessment/")
def anxiety_assessment():
    return render_template('Anxiety_Exam.html')	

@app.route("/anxiety_assessment/results/")
def anxiety_assessment_results():
    return render_template('anxiety_assessment_results.html'); 

@app.route("/depression_assessment/")
def depression_assessment():
    return render_template('Depression_Exam.html')

@app.route("/depression_assessment/results/")
def depression_assessment_results():
    return render_template('depression_exam_results.html'); 
					
