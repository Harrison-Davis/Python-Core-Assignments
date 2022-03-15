from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def add_visit():
    if 'numvisits' in session:
        session['numvisits'] += 1
    else:
        session['numvisits'] = 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)