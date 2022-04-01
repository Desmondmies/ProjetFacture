import os
from flask import Flask, render_template

TEMPLATE_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def test():
    return render_template('./test_link_css.html')


if __name__ == "__main__":
	try:
		app.run(debug = True)
	except KeyboardInterrupt:
		print("Application terminé.")
