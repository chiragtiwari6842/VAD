from flask import Flask, render_template, jsonify
import numpy as np
import pyaudio
import threading
from collections import deque

app = Flask(__name__)

CHUNK = 1024 
FORMAT = pyaudio.paFloat32 
CHANNELS = 1 
RATE = 16000  
FRAME_LENGTH = 2048  
THRESHOLD = 2.0 

p = pyaudio.PyAudio()

audio_buffer = deque(maxlen=FRAME_LENGTH)
warning_counter = 0
consecutive_counter = 0
warnings_issued = 0
warnings_list = []

def extract_energy(audio_frame):
    return np.sum(np.abs(audio_frame**2))

def vad_real_time():
    global warning_counter, consecutive_counter, warnings_issued, warnings_list
    audio_stream = []
    
    def callback(in_data, frame_count, time_info, status):
        global warning_counter, consecutive_counter, warnings_issued
        audio_frame = np.frombuffer(in_data, dtype=np.float32)
        audio_stream.append(audio_frame)
        audio_buffer.extend(audio_frame)

        if len(audio_buffer) == FRAME_LENGTH:
            audio_frame_np = np.array(audio_buffer)
            energy = extract_energy(audio_frame_np)

            if energy > THRESHOLD:
                consecutive_counter += 1
            else:
                consecutive_counter = 0 

            if warnings_issued < 3:
                if consecutive_counter == 2:
                    warnings_issued += 1
                    warnings_list.append(f"Warning {warnings_issued}: Threshold crossed! Excessive speech detected.")
                    consecutive_counter = 0 
            elif warnings_issued == 3:
                if consecutive_counter == 1:
                    warnings_list.append("Sorry, you couldn't finish. Exiting...")
                    return (None, pyaudio.paComplete)  # Stop the stream

        return (in_data, pyaudio.paContinue)

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

    stream.start_stream()

    try:
        while stream.is_active():
            pass 
    except Exception as e:
        print(f"Error: {e}")
    finally:
        stream.stop_stream()
        stream.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_warnings')
def get_warnings():
    global warnings_list
    return jsonify(warnings=warnings_list)

threading.Thread(target=vad_real_time, daemon=True).start()

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
