# pip install gtts

from gtts import gTTS
import os

def text_to_mp3(text_file, language='en'):
    # Read the text file
    with open(text_file, 'r') as file:
        text = file.read()

    # Convert text to speech
    tts = gTTS(text, lang=language)

    # Save the audio file
    audio_file = text_file.replace('.txt', '.mp3')
    tts.save(audio_file)
    print(f"Saved audio file as {audio_file}")

# Replace 'yourfile.txt' with the path to your text file
text_to_mp3('yourfile.txt')
