from pytube import YouTube
from converter import convert


def download_audio_from_youtube(url):
    """
    Downloads audio from YouTube video using the provided URL.
    """
    youtube = YouTube(url)
    audio_stream = youtube.streams.filter(only_audio=True).first()
    output_file = youtube.title + ".mp3"
    audio_stream.download(output_path=".", filename=output_file)
    print(youtube.title + " downloaded successfully!")

    # convert mp3 to wav
    convert(output_file)
