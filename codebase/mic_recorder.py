import sounddevice as sd
from scipy.io.wavfile import write

def mic_recorder(path="audio/temp.wav", duration=5, fs=44100):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(path, fs, recording)
    return path
