import os
<<<<<<< Updated upstream
from flask import Flask

app = Flask(__name__)
=======
from flask import Flask, render_template #render_template permet d'utiliser directement du code HTML et de lui passer en paramètre des variables

from Python.Manager.Artisan import Artisan
from Python.Manager.Client_mng import Client_mng

from Python.Client import Client
from Python.Invoice import Invoice


HTML_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)
>>>>>>> Stashed changes

@app.route("/")
def test():
	return "<h1>TEST HELLO</h1>"

def initialisation():
    artisan = Artisan() #On charge les données de l'artisan
    client_mng = Client_mng()
    #On charge les données des factures
    #On charge les données des devis
    
if __name__ == "__main__":
<<<<<<< Updated upstream
	print("test github/atom")
	try:
		#os.system('flask run')
		app.run(debug=True)
	except KeyboardInterrupt:
		print("Application terminé.")
=======
    initialisation()
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
>>>>>>> Stashed changes
