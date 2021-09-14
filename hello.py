from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola, mundo!'.upper()

@app.route('/bye')
def otro():
    return "Adiós mundo cruel!"