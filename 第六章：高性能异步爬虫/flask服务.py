from flask import Flask
import time

app = Flask(__name__)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello Bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello Jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello Tom'

if __name__ == '__main__':
    app.run(threaded=True)