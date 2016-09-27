from flask import Flask, render_template
import utils.occupationFunctions

app = Flask(__name__)

@app.route("/occupations")
def occupations():
    return render_template("occTable.html",occList=utils.occupationFunctions.finalList(),occupation=utils.occupationFunctions.pickOccupation())

@app.route("/ilovemrbrown")
def crew():
    return app.send_static_file("crew.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
