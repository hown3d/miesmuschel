import wave

import pyaudio

from .const import CHUNK, CHANNELS


def play_audio( wave_file_path: str):
    p = pyaudio.PyAudio()
    with wave.open(wave_file_path, 'rb') as wf:
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=CHANNELS,
                        rate=wf.getframerate(),
                        output=True)  # Open stream (2)

        while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
            stream.write(data)
    # Close stream
    stream.close()

    # Release PortAudio system resources
    p.terminate()
