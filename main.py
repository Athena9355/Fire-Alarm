# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")






@app.route('/aadya')
def aadya():
    return render_template("aadya.html")

@app.route('/athena')
def athena():
    return render_template("athena.html")

@app.route('/gaurish')
def gaurish():
    return render_template("gaurish.html")

@app.route('/karthik')
def karthik():
    return render_template("karthik.html")

@app.route('/siya')
def siya():
    return render_template("siya.html")



@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/About Us/')
def aboutus():
    return render_template("About Us.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
