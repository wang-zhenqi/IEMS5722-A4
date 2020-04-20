from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iems572230347'
app.debug=True

socketio = SocketIO(app)

@app.route("/api/a4/broadcast_room", methods=["POST"])
def broadcast_room():
    result = {}
    chatroom_id = int(request.form.get('chatroom_id', '-1'))
    name = request.form.get('name', '')
    message = request.form.get('message', '')
    timestamp = request.form.get('timestamp', '')
    if chatroom_id == -1 or name == '' or message == '' or timestamp == '':
        result['message'] = 'Invailid Parameter'
        result['status'] = 'Error'
    else:
        result['message'] = message
        result['name'] = name
        result['timestamp'] = timestamp[:-3]
        result['status'] = 'OK'
    print("emit message:" + str(result) + "to chatroom " + str(chatroom_id), flush=True)
    socketio.emit('new_message', result, room=chatroom_id)
    return jsonify(result)

@socketio.on('connect')
def connect_handler():
    print("connected", flush=True)
    emit("select_room")

@socketio.on('disconnect')
def disconnect_handler():
    print("disconnect", flush=True)

@socketio.on('join')
def on_join(data):
    chatroom_id = data['chatroom_id']
    print("join the room " + str(chatroom_id), flush=True)
    join_room(chatroom_id)

@socketio.on('leave')
def on_leave(data):
    chatroom_id = data['chatroom_id']
    print("leave the room " + str(chatroom_id), flush=True)
    leave_room(chatroom_id)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8001)
