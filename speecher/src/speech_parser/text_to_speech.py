import io
import pathlib
import sys

import gtts.lang
from gtts import gTTS

from detect_language import detect_language


# Function to convert text to speech and save the output in WAV format
def text_to_speech(input_text: str, lang: str) -> io.BytesIO:
    tts = gTTS(input_text, lang=lang)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    return buf


def get_languages():
    for key, lang in gtts.lang.tts_langs().items():
        print(f"Specifying key: {key} uses langugage: {lang}")


def persist_tts(buf: io.BytesIO, filename):
    with pathlib.Path(filename) as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write_bytes(buf.getbuffer())


def usage() -> str:
    args = sys.argv
    return f'''
    Usage:
    {args[0]} text 
    '''


def main(text: str):
    detected_lang = detect_language(text)
    print(f"detected language: {detected_lang.name}")
    lang_code = detected_lang.iso_code_639_1.name.lower()
    tts_buf = text_to_speech(text, lang_code)
    file_name = "hello.wav"
    print(f"saving audio to {file_name}")
    persist_tts(buf=tts_buf, filename=file_name)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        usage()
        exit(1)
    else:
        text = args[1]
    main(text)
