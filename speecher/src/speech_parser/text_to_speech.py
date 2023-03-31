import io
import logging
import pathlib
import sys
import tempfile
from typing import Optional

import gtts.lang
from gtts import gTTS

from src.audio import convert
from .detect_language import detect_language


def text_to_speech(msg: str) -> Optional[str]:
    detected_lang = detect_language(msg)
    if detected_lang is None:
        return None

    print(f"detected language: {detected_lang.name}")
    lang_code = detected_lang.iso_code_639_1.name.lower()
    filepath = execute_tts(msg, lang_code)
    return convert.convert_mp3_to_wave(filepath)


def execute_tts(input_text: str, lang: str) -> str:
    temp = tempfile.NamedTemporaryFile(suffix="tts.mp3", delete=False)
    tts = gTTS(input_text, lang=lang)
    tts.write_to_fp(temp)
    temp.close()
    return temp.name


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
    tts_filepath = text_to_speech(text)
    if tts_filepath is None:
        logging.error("could not execute text to speech")
    print(f"saving audio to {tts_filepath}")


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        usage()
        exit(1)
    else:
        text = args[1]
    main(text)
