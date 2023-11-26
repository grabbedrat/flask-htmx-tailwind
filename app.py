from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import librosa
from io import BytesIO
from pydub import AudioSegment
from scipy.io.wavfile import write
import numpy as np
from scipy.io.wavfile import read
from pydub import AudioSegment

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize buffer to accumulate audio data
audio_buffer = BytesIO()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/audio_stream')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/audio_stream')
def handle_disconnect():
    print('Client disconnected')
    process_and_save_audio()  # Process and save when client disconnects

@socketio.on('audio_data', namespace='/audio_stream')
def handle_audio_data(audio_data):
    try:
        print(f"Received audio data from client, length: {len(audio_data)}")
        audio_buffer.write(audio_data)
        print(f"Data written to audio_buffer, length: {len(audio_buffer.getvalue())}")
    except Exception as e:
        print(f"Error receiving/storing audio data: {e}")

def process_and_save_audio():
    try:
        print(f"Data in audio_buffer before read, length: {len(audio_buffer.getvalue())}")
        audio_buffer.seek(0)
        audio_data = audio_buffer.read()
        print(f"Data read from audio_buffer, length: {len(audio_data)}")
        
        # Check if audio_data is empty
        if not audio_data:
            print("Audio data is empty")
            return
        
        # Write the audio data to a temporary file
        with open('temp.ogg', 'wb') as f:
            f.write(audio_data)
        
        # Convert the audio data from Ogg to WAV format
        audio = AudioSegment.from_ogg('temp.ogg')
        audio.export('temp.wav', format='wav')
        
        # Read the audio data from the temporary file
        sample_rate, audio = read('temp.wav')
        
        # Rest of the code...
    except Exception as e:
        print(f"Error processing/saving audio: {e}")

if __name__ == '__main__':
    socketio.run(app, debug=True)