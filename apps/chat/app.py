
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO,emit
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, engineio_logger=True)
socketio.init_app(app, cors_allowed_origins="*")


@app.route('/chat')
def sessions():
    return jsonify({0:'data'})


@socketio.on('my event', '/socket.io')
def test_message(message):
    emit('my response', {'data':message['data']})


@socketio.on('my broadcast event','/socket.io')
def test_message1(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect','/socket.io')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect','/socket.io')
def test_disconnect():
    print('client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')