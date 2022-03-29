import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "<h1>TEST HELLO</h1>"


"""
NE FONCTIONNE PAS, le fichier doit être appelé app.py pour pouvoir exécuter flask run
sinon il faut définir une variable d'environnement, FLASK_APP = nomdufichier
sur mon windows ça à pas l'air de fonctionner, donc passage sur app.py

if __name__ == "__main__":
    os.system('set FLASK_APP=test')
    os.system('flask run')
"""