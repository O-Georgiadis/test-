from flask import Flask, render_template, request

app = Flask(__name__) #__name__ refers to the name of the current file



#Decorator (a special type of function that modifies another function)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "world")  #it returns: hello, {{name}} or if no name is inserted: hello, world
    return render_template("greet.html", name=name) 