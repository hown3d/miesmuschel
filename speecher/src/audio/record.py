import sys
import tempfile
import threading
import wave
from queue import Queue

import pyaudio

from .const import CHANNELS, FORMAT, RATE, CHUNK


def record_audio_to_wave(cancel_event: threading.Event, queue: Queue):
    p = pyaudio.PyAudio()

    with tempfile.NamedTemporaryFile(suffix="record.wav", delete=False) as temp:
        with wave.open(temp.name, "wb") as wf:
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setnchannels(CHANNELS)
            wf.setframerate(RATE)

            stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

            print('Recording...')
            while not cancel_event.is_set():
                wf.writeframes(stream.read(CHUNK))
            print('Done')

            stream.close()
            wf.close()
            p.terminate()

    # write filename into queue to communicate to process
    queue.put(temp.name)


def start_record(cancel_event: threading.Event, queue: Queue):
    record_thread = threading.Thread(target=record_audio_to_wave, args=(cancel_event, queue))
    record_thread.start()


if __name__ == '__main__':
    cancel = threading.Event()
    start_record(cancel_event=cancel, queue=Queue(maxsize=0))
    print("waiting for \"exit\"")
    for line in sys.stdin:
        if line.rstrip() == "exit":
            cancel.set()
            break
    cancel.wait()
    print("finished recording")
