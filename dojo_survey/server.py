from unicodedata import name
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def submit():
    session['name'] = request.form['name'] 
    session['location'] = request.form['location'] 
    session['language'] = request.form['language'] 
    session['comments'] = request.form['comments'] 
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template("results.html" )

@app.route('/form')
def go_back(): 
    return render_template('form.html', )


if __name__=='__main__':
    app.run(debug=True)

