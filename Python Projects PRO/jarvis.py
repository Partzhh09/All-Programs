import pyttsx3
import os

# Define the folder where you want to save the audio file
folder_path = 'audio_files'  # Folder name
if not os.path.exists(folder_path):  # Check if the folder exists
    os.makedirs(folder_path)  # Create the folder if it doesn't exist

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 120)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Set the text to be spoken
text = "vimal lick my dick"

# Define the full file path to save the audio
file_path = os.path.join(folder_path, 'jarvis_output.mp3')

# Save speech to a file
engine.save_to_file(text, file_path)

# Run the engine to process the speech
engine.runAndWait()

print(f"The audio has been saved in the folder '{folder_path}' as 'jarvis_output.mp3'.")
