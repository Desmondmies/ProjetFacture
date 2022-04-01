import os
from flask import Flask, render_template

TEMPLATE_DIR = os.path.abspath('./WEB/HTML')
 
app = Flask(__name__, template_folder=TEMPLATE_DIR) 

@app.route("/")
def test():
	return """
	<form action="/test_btn" method="post">
	<button type="submit">Page 2 !</button>
	</form>
	"""

@app.route("/test_btn", methods=['POST'])
def test_btn_click():
	return render_template("./page2.html")

if __name__ == "__main__":
	print("test github/atom")
	try:
		#os.system('flask run')
		app.run(debug=True)
	except KeyboardInterrupt:
		print("Application terminé.")
