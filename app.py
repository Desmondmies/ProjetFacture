from flask import Flask, render_template
#render_template permet d'utiliser directement du code HTML
#et de lui passer en paramètre des variables
app = Flask(__name__)

dico_client = {"Nom" : "noooom...",
                "Prenom" : "...bril",
                "Tel" : "06 06 06 06 06",
                "Mail" : "machin@qqchmail.fr",
                "Description" : "Riche client qui vient souvent etc..........."}

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/autre")
def autre():
    return render_template("dynamique_page.html", posts = [dico_client]) #posts = variable à passer en paramètre à notre page HTML



if __name__ == "__main__":
    print("test github/atom")
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
