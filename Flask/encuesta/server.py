from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key="clave super secreta de la encuesta"

@app.route("/")
def encuesta():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def guardaDatos():

    session['usuario'] = request.form['nombre'] 
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect("/result")

@app.route("/result")
def resultado():
    return render_template("bienvenido.html")

if __name__ == "__main__":
    app.run(debug=True)