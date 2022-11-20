from flask import Flask, render_template, session, redirect
app = Flask(__name__)

app.secret_key="clave ultra secreta"

@app.route("/")
def contador():
    if "visitas" not in session:
        session["visitas"] = 0 
    else:
        session["visitas"] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def destruir():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)