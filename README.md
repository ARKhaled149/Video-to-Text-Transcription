# Video to Text Transcription Script

## Overview

This repository contains a Python script designed to transcribe video files into text using the Whisper model. This tool is particularly useful for generating subtitles or captions, making video content more accessible.

## Prerequisites

Before using this script, ensure you have the following:

- **Python**: Installed on your system.
- **Whisper Model**: Installed and accessible from the command line.
- **Basic Command-Line Knowledge**: To execute the script and manage file paths.

## Script Features

The script performs the following tasks:

1. **Path Configuration**: Allows you to specify the video file and the destination directory for the output text file using raw string literals to handle file paths correctly.

2. **Directory Management**: Automatically checks and creates the output directory if it does not already exist.

3. **Transcription Execution**: Utilizes the Whisper model to process the video file and generate a text transcription.

4. **Output Notification**: Confirms completion of the transcription process with a console message.

## How to Use

1. **Update File Paths**: Modify the `video_file_path` and `output_directory` variables in `transcribe-all.py` to reflect your local setup.

2. **Run the Script**: Execute the script via the command line:

    ```bash
    python transcribe-all.py
    ```

3. **View Output**: The transcribed text will be saved in the specified output directory.

## Code Explanation

```python
import os
import subprocess

# Define the path to your video file and the output directory using raw strings
video_file_path = r"video_path"
output_directory = r"output_text_path"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Transcribe the video file using Whisper
command = f'whisper "{video_file_path}" --model large --output_dir "{output_directory}" --output_format txt'
subprocess.run(command, shell=True)

print("Transcription completed successfully.")
```

### Key Components

- **Raw String Literals**: Used for file paths to avoid issues with escape characters.
- **Directory Creation**: Ensures the output directory is in place to prevent errors.
- **Whisper Command**: Configures the transcription process, specifying the model size and output format.
- **Subprocess Execution**: Runs the transcription command in the shell.
- **Completion Message**: Provides user feedback upon successful completion.

## Options

- **Model Size**: The script uses a `large` model by default but can be adjusted to fit other available sizes depending on your requirements like `medium` and `small`, however the performance and accuracy are affected.
- **Output Format**: Currently set to output text (`txt`), but can be adapted if Whisper supports other formats.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!
