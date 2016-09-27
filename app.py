from flask import Flask, render_template
import util.occupationFunctions

app = Flask(__name__)

@app.route("/occupations")
def occupations():
    return render_template("occTable.html",occList=util.occupationFunctions.finalList(),occupation=util.occupationFunctions.pickOccupation())

if __name__ == "__main__":
    app.debug = True
    app.run()
