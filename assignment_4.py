from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iems572230347'

socketio = SocketIO(app)

@app.route("/api/a4/broadcast_room", methods=["GET"])
def broadcast_room():
    chatroom_id = int(request.args.get('chatroom_id'))
    message = request.args.get('message')
    #socketio.emit(...)

@socketio.on('my event')
def my_event_handler(data):
    emit(...)

@socketio.on('join')
def on_join(data):
    join_room(chatroom_id)

@socketio.on('leave')
def on_leave(data):
    leave_room(chatroom_id)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8001)
