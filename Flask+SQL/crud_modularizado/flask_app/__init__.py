from flask import Flask

app = Flask(__name__)

app.secret_key = "Esto puede tener cualquier texto"