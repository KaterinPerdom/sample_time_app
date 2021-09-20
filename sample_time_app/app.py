from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello Katerine :D "


@app.route('/time')
def time():
    today = date.today()
    return (str(today))


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
