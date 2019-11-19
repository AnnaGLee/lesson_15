from flask import Flask, render_template

#wir legen app objekt an mit dem wir die webanwedung konfigurieren können
app = Flask(__name__)

counter = 0

#wir definieren eine route via dekorator das mit dem @
@app.route("/")

def index():
    global counter #global weil wir counter innerhalb der Funktion verwenden wollen
    counter +=1
    #rendern vom template(Vorlage) index.html im Verzeichnis templates
    return render_template("index.html", zaehler=counter) #davon return Hello you little SmartNinja {0}".format(1+1)

@app.route("/about")
def about():
    return render_template("about.html")

#wenn dieses modul das hauptmodul ist dann starten wir flask
if __name__== "__main__":
    app.run()