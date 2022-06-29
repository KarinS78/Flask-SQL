from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hey Gabi"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        name = request.form["nm"]
        session["name"] = name
        flash("Login Succcesfull!")
        return redirect(url_for("name"))
    else:
        if "name" in session:
            flash("Already Logged In!")
            return redirect(url_for("name"))

        return render_template("login.html")

@app.route('/name')
def name():
    if "name" in session:
        user = session["name"]
        return f"hello <h1>{name}</h1> :)"
    else: 
        flash("Already Logged In!")
        return  render_template("user.html", name = name)

@app.route("/logout")
def logout():
    if "name" in session:
        user = session["name"]
        flash("you have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run()