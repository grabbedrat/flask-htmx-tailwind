from flask import Flask, render_template
from flask_socketio import SocketIO
import redis
import threading

app = Flask(__name__)
# Enable CORS for all domains on all routes
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)
pubsub = redis_client.pubsub()
pubsub.subscribe('audio_channel')

@socketio.on('connect', namespace='/audio_stream')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/audio_stream')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('audio_data', namespace='/audio_stream')
def handle_audio_data(audio_data):
    print(f"Received audio data from client")
    redis_client.publish('audio_channel', audio_data)

def listen_for_audio_data():
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received audio data from Redis")
            audio_data = message['data']

# Create and start a new thread for the listener
listener_thread = threading.Thread(target=listen_for_audio_data)
listener_thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
