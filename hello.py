from flask import Flask

app = Flask(__name__)

def make_bold(fx):
    def wrapper():
        return "<em>" + fx() + "</em>"
    return wrapper

def under_lined(fx):
    def wrapper():
        return "<u>" + fx() + "</u>"
    return wrapper



# Decorator function is route which live under app which is decleare under flask class
@app.route("/")
def hello_world():
    return '<h1 style="text-align: center"> Hello , world</h1> \
        <p> This is Kitten </p>'  
 
@app.route("/bye")
@make_bold
@under_lined
def func():
    return "<p> byee <p/>"

@app.route("/username/<path:name>")
def greet(name):
    return f"Hello {name}!" 

if __name__ ==  "__main__":
    app.run(debug=True) 

