import sys
import threading
import wave

import pyaudio

FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
CHUNK = 1024


def record_audio_to_wave(cancel: threading.Event):
    with wave.open('output.wav', 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        while not cancel.is_set():
            wf.writeframes(stream.read(CHUNK))
        print('Done')

        stream.close()
        p.terminate()



if __name__ == '__main__':
    cancel = threading.Event()
    record_thread = threading.Thread(target=record_audio_to_wave, args=(cancel,))
    record_thread.start()
    print("waiting for \"exit\"")
    for line in sys.stdin:
        if line.rstrip() == "exit":
            cancel.set()
            break

    cancel.wait()
    print("finished recording")
