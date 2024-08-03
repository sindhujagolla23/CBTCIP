import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(duration, sample_rate=44100, filename="output.wav"):
    print(f"Recording for {duration} seconds...")

    # Record audio
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save the recording as a WAV file
    write(filename, sample_rate, recording)
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    duration = 10  # seconds
    record_audio(duration)
