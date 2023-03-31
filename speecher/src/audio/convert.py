from pydub import AudioSegment
import tempfile
import os.path


def convert_mp3_to_wave(src_path: str) -> str:
    sound = AudioSegment.from_mp3(src_path)
    dest_path = f"{tempfile.gettempdir()}{os.path.sep}tts.wav"
    sound.export(dest_path, format="wav")
    return dest_path
