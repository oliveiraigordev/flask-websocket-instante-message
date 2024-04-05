from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


@app.get('/')
def index():
    return render_template('index.html', host="http://127.0.0.1:5000")


@socketio.on('message')
def message(msg):
    socketio.emit('message', msg)


if __name__ == '__main__':
    socketio.run(app, debug=True)
