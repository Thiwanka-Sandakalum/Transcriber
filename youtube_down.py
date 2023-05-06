from pytube import YouTube
import subprocess
from tqdm import tqdm

def download_audio_from_youtube(url):
    """
    Downloads audio from YouTube video using the provided URL.
    """
    youtube = YouTube(url)
    audio_stream = youtube.streams.filter(only_audio=True).first()
    output_file = youtube.title + ".mp3"
    audio_stream.download(output_path=".", filename=output_file)
    print(youtube.title + " downloaded successfully!")
    file_name = youtube.title
    convert(file_name)


def convert(file_name):
    # convert mp3 to wav
    print("converting.............")
    subprocess.call(['ffmpeg', '-i', f'{file_name}.mp3', '-ar',
                    '16000', '-ac', '1', '-c:a', 'pcm_s16le', 'output.wav'])

    # remove downloaded mp3 file
    subprocess.run(['rm', '-f', f'{file_name}.mp3'])

    # close the progress bar
    return f'{file_name}.wav'
