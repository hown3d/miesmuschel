import logging
import os
import queue
import signal
import threading

import chatter.client
from audio.play import play_audio as play_audio
from audio.record import start_record
from speech_parser.speech_to_text import speech_to_text
from speech_parser.text_to_speech import text_to_speech

message_service = chatter.client.MessageService("http://localhost:8080")

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

def wait_for_exit_input(cancel: threading.Event):
    if input("press s to stop recording\n") == "s":
        cancel.set()


def record_and_get_outputfile() -> str:
    q = queue.Queue()
    cancel = threading.Event()
    start_record(cancel, queue=q)
    wait_thread = threading.Thread(target=wait_for_exit_input, args=(cancel,))
    wait_thread.start()
    cancel.wait()
    output_filepath = q.get(block=True)
    return output_filepath


def eventloop():
    output_fp = record_and_get_outputfile()
    text = speech_to_text(output_fp)

    # remove temporary file containing audio record
    # not neccessary anymore because we got the text already
    os.remove(output_fp)

    print(f"you said: {text}")
    answer = get_chat_answer(text)
    print(f"chat gpt answered: {answer}")
    tts_filepath = text_to_speech(answer)
    if tts_filepath is None:
        logging.error("could not execute text to speech")
        return
    play_audio(tts_filepath)

    # remove temporary file containing text to speech audio
    # not neccessary anymore because we played the audio on speakers
    os.remove(tts_filepath)


def get_chat_answer(msg: str) -> str:
    return message_service.get(msg)


def signal_handler(signal, frame):
    print('Terminated by CTRL/C')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    while True:
        operation = input("type 'r' to start record\n")
        match operation:
            case "r": eventloop()


if __name__ == '__main__':
    main()
