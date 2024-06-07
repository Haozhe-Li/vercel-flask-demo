import flask
import time

app = flask.Flask(__name__)

@app.route('/')
def index():
    time.sleep(11)
    # sleep
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()