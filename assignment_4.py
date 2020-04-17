from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iems572230347'
app.debug=True

socketio = SocketIO(app)

@app.route("/api/a4/broadcast_room", methods=["GET"])
def broadcast_room():
    result = {}
    chatroom_id = int(request.args.get('chatroom_id'))
    message = request.args.get('message')
    if not (chatroom_id and message):
        result['message'] = 'Invailid Parameter'
        result['status'] = 'Error'
        return jsonify(result)
    result['chatroom_id'] = chatroom_id
    result['message'] = message
    socketio.emit('new_message', {'text': 'message'}, room=chatroom_id)
    return jsonify(result)

@socketio.on('my event')
def my_event_handler(data):
    emit(...)

@socketio.on('join')
def on_join(data):
    chatroom_id = data['chatroom_id']
    print(chatroom_id)
    join_room(chatroom_id)

@socketio.on('leave')
def on_leave(data):
    chatroom_id = data['chatroom_id']
    print(chatroom_id)
    leave_room(chatroom_id)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8001)
