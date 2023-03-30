import whisper

model = whisper.load_model("base")

def speech_to_text(audio_file_path: str) -> str:
    result = model.transcribe(audio_file_path)

    return result["text"]

