from flask import Flask, render_template
import occupation

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('occuHomePage.html')

@app.route('/occupations')
def occupations():
    return render_template('occu-table.html', description = occupation.randomPick(), table = occupation.stringDict())


if (__name__ == "__main__"):
    app.debug = True
    app.run()
