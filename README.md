
# Application Documentation

## Introduction

This application is a command-line tool that allows users to transcribe audio from YouTube videos or podcasts. The application takes a YouTube URL or a podcast URL as input and produces a transcription in various formats such as SRT, JSON, text, VTT, or LRC. The application runs exclusively in a terminal environment.

## Files

The application consists of several Python files:

1. `main.py`: This is the main file that contains the entry point of the application. It handles user input, downloads the audio from the specified URL, and triggers the transcription process.
2. `Transcriber.py`: This file contains the logic for building the command to transcribe the audio. It interacts with the underlying speech-to-text engine to generate the transcription in different formats.
3. `youtube_down.py`: This file contains the code to download audio from a YouTube video. It uses the YouTube API or a suitable library to fetch the audio content.
4. `pod_down.py`: This file contains the code to download audio from a podcast. It utilizes appropriate libraries or APIs to retrieve the audio content from the provided podcast URL.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the application files are located.
3. Run the following command: `python main.py`
4. The application will prompt you for the type of operation you want to perform: transcription or summarization. Enter `T` for transcription or `S` for summarization.
5. Next, the application will ask you to specify the source of the audio: YouTube or Google Podcast. Enter `Y` for YouTube or `P` for Google Podcast.
6. If you selected YouTube, enter the URL of the YouTube video when prompted. If you selected Google Podcast, enter the URL of the podcast.
7. The application will download the audio from the specified source and initiate the transcription process.
8. Once the transcription is complete, the application will generate the desired output format (SRT, JSON, text, VTT, or LRC) based on your selection.
9. The generated transcription file will be saved in the current directory.
10. The temporary audio file used for transcription will be cleaned up automatically.

## Dependencies

The application requires the following dependencies to be installed:

- Python 3.x
- Libraries: `subprocess`, `youtube_dl`, (additional dependencies for audio-to-text conversion, e.g., `speechRecognition`, `pydub`, or any suitable library)

Ensure that all the required dependencies are installed before running the application.

## Limitations

- The application is designed to run in a terminal environment only.
- It assumes that the necessary dependencies and libraries for audio-to-text conversion are properly installed.
- The application currently supports YouTube and Google Podcast as the audio sources. Support for other platforms may be added in future updates.

## Future Enhancements

- Support for additional audio sources and formats.
- Integration with more speech-to-text engines for improved accuracy.
- Option to specify the output directory and file name for the generated transcription.
- Error handling and better user feedback during the download and transcription process.
- Implementation of the summarization feature for generating summaries of audio content.
- Improved command-line interface with options and flags for customization.

Please note that this documentation provides an overview of the application and its current state. For detailed implementation and technical details, refer to the source code of the respective files.
