from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello khematat"

@app.route('/about')
def about():
    return "<h1>About Me</h1>"

@app.route('/admin')
def profile():
    return "<h1>Sawasdeekub Admin</h1>"

@app.route('/user/<name>/<age>')
def member(name,age):
    return "<h1>Hello member : {} , Age : {}</h1>".format(name,age)

if __name__ == "__main__":
    app.run()