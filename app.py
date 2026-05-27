from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

button_status = False

@app.route('/')
def index():
    return render_template('index.html', status=button_status)

@socketio.on('connect')
def handle_connect():
    emit('status_update', {'status': button_status})

@socketio.on('toggle_button')
def handle_toggle():
    global button_status
    button_status = not button_status
    emit('status_update', {'status': button_status}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)