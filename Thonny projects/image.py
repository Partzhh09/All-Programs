import pyttsx3
from gtts import gTTS
import os

def pyttsx3_tts(text):
    """ Function to use pyttsx3 for offline TTS """
    try:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Set properties like speed and voice
        engine.setProperty('rate', 150)  # Speed (words per minute)
        voices = engine.getProperty('voices')

        # Set voice (you can change the index for different voices)
        engine.setProperty('voice', voices[1].id)  # You can try changing the index

        # Convert text to speech
        engine.say(text)

        # Wait until speech is finished
        engine.runAndWait()
    except Exception as e:
        print(f"Error using pyttsx3: {e}")

def gtts_tts(text):
    """ Function to use gTTS for online TTS """
    try:
        # Language in which you want to convert the text
        language = 'en'

        # Passing the text and language to the engine
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the converted audio to a file
        tts.save("output_jarvis.mp3")

        # Play the converted file
        os.system("start output_jarvis.mp3")  # Windows-specific
        # On MacOS/Linux, use: os.system("mpg321 output_jarvis.mp3") or a similar command
    except Exception as e:
        print(f"Error using gTTS: {e}")

def main():
    # Text to be converted to speech
    text = "Hello, welcome to devil's laptop"

    # Choose the TTS engine
    print("Choose TTS engine:")
    print("1. Offline (pyttsx3)")
    print("2. Online (gTTS)")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        pyttsx3_tts(text)
    elif choice == '2':
        gtts_tts(text)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
