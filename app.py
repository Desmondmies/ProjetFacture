import os
from flask import Flask, render_template

TEMPLATE_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def test():
    return render_template('./test_link_css.html')

@app.route("/Formulaire")
def page_formulaire():
    return render_template('./PageFormulaire.html')

@app.route("/Artisan")
def page_artisan():
    return render_template('./PageArtisan.html')

@app.errorhandler(404)
def not_found(arg):
    return "Développement de la page en cours."

if __name__ == "__main__":
	try:
		app.run(debug = True)
	except KeyboardInterrupt:
		print("Application terminé.")
