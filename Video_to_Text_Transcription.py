import os
import subprocess

# Define the path to your video file and the output directory using raw strings
video_file_path = r"C:\Users\Abdel\Desktop\Immersive Insiders\Images and GIFs\Learn How To Create Spatial Maps and Place AR Content  Immersal SDK\Learn How To Create Spatial Maps and Place AR Content ｜ Immersal SDK.mp4"
output_directory = r"C:\Users\Abdel\Desktop\Immersive Insiders\Images and GIFs\Learn How To Create Spatial Maps and Place AR Content  Immersal SDK"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Transcribe the video file using Whisper
command = f'whisper "{video_file_path}" --model large --output_dir "{output_directory}" --output_format txt'
subprocess.run(command, shell=True)

print("Transcription completed successfully.")
