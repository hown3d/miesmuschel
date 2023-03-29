import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to convert text to speech and save the output in WAV format
def text_to_speech(input_text, file_name):
    # Set the audio format to WAV
    audio_format = 'wav'

    # Convert the input text to speech and save the output in the desired audio format
    engine.save_to_file(input_text, f"{file_name}.{audio_format}")
    engine.runAndWait()

def change_voice(language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

if __name__ == '__main__':
    change_voice("de_DE")
    # Invoke the function with the input text and file name
    text_to_speech("Hallo, wie geht's Ihnen?", "hello")
