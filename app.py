from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    data={"name":"khematat","age":30,"salaty":"300000"}
    return render_template("index.html",mydata=data)

@app.route('/about')
def about():
    products = ['shirt','skirt','T-shirt','pant','hoodie']
    return render_template("about.html",myproducts = products)

@app.route('/admin')
def profile():
    # name and age
    return render_template("admin.html")



if __name__ == "__main__":
    app.run(debug=True)