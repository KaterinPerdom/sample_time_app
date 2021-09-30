from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Katerine :D!'

@app.route('/time')
def time():
    now = datetime.now()
    time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return time



app.run(host='0.0.0.0',
        port=8080,
        debug=True)
