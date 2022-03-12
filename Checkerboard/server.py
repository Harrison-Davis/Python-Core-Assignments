from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/displaybox/<int:num>')
def box(num): 
    return render_template("index.html", num=num) 

#keep this at the bottom, below all routes
if __name__=='__main__':
    app.run(debug=True)   #runs the app in debug mode