import sys
from pyaudio import paInt16
from typing import Final

FORMAT: Final[int] = paInt16
CHANNELS: Final[int] = 1 if sys.platform == 'darwin' else 2
RATE: Final[int] = 44100
CHUNK: Final[int] = 1024
