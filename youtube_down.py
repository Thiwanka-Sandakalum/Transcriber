from pytube import YouTube
from converter import convert_audio_to_wav
import os

output_path = "model/output.wav"

def download_audio_from_youtube(url):
    """
    Downloads audio from YouTube video using the provided URL.
    """
    youtube = YouTube(url)
    audio_stream = youtube.streams.filter(only_audio=True).first()
    output_file = youtube.title + ".mp3"
    audio_stream.download(output_path=".", filename=output_file)
    print(youtube.title + " downloaded successfully!")

    # Convert mp3 to wav
    convert_audio_to_wav(input_file=output_file, output_file=output_path)

    os.remove(output_file)
