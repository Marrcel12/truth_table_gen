from flask import Flask, render_template,request,jsonify
from main import main_fun
app = Flask(__name__)

@app.route("/")
def sign_up():
    return render_template("index.html")
@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    return main_fun(projectpath)