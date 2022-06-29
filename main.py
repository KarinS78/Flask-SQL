from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/<name>')
def user(name):
    if name == "gabi":
        return redirect('/home')
    else:
        return f"hello {name} :)"

if __name__ == '__main__':
    app.run()