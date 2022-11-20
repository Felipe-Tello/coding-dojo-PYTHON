from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def ocho():
    return render_template("8por8.html")

@app.route("/4")
def cuatro():
    return render_template("8por4.html")

@app.route("/<int:num>/<int:num2>")
def inicio(num, num2):
    return render_template("index.html",num=num,num2=num2)

if __name__ == "__main__":
    app.run(debug=True)
