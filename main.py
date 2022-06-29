from crypt import methods
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        usr = request.form["nm"]
        return redirect(url_for("name", usr = name))
    else:
        return render_template("login.html")

# @app.route('/<name>')
# def name(name):
#     if name == "gabi":
#         return redirect('/home')
#     elif name == "login":
#         return redirect(url_for("login"))
#     else:
#         return f"hello <h1>{name}</h1> :)"




if __name__ == '__main__':
    app.run()