# Copyright (C) 2023 Thiwanka Sandakalum. All rights reserved.
# Developed by Thiwanka Sandakalum

from youtube_down import download_audio_from_youtube
from pod_down import PodcastDownloader
# from Transcriber import transcribe_audio

def download_and_transcribe():
    user_input_1 = input("If you want to transcribe press T or if you want to summarize press S: ").upper()

    while user_input_1 not in ['T', 'S']:
        print("Invalid input. Please enter T to transcribe or S to summarize.")
        user_input_1 = input("If you want to transcribe press T or if you want to summarize press S: ").upper()

    user_input_2 = input("For YouTube press Y or for Google Podcast press P: ").upper()

    while user_input_2 not in ['Y', 'P']:
        print("Invalid input. Please enter Y for YouTube or P for Google Podcast.")
        user_input_2 = input("For YouTube press Y or for Google Podcast press P: ").upper()

    if user_input_2 == "Y":
        url = input("Enter YouTube URL: ")
        download_audio_from_youtube(url)
        file_name = download_audio_from_youtube.output_file

    else:
        url = input("Enter Podcast URL: ")
        podcast = PodcastDownloader(url)
        podcast.get_soup()
        podcast.get_episodes()

        while True:
            try:
                selected_episode = int(input("Enter episode number you want to download: "))
                file_name = podcast.download_episode(selected_episode)
                break
            except ValueError:
                print("Invalid input. Please enter a valid episode number.")

    if user_input_1 == "T":
        transcribe_audio("base", file_name)
        print(f"Transcription complete. Output file: {file_name}.txt")

    else:
        # summarize_audio function to be implemented
        pass

if __name__ == "__main__":
    download_and_transcribe()
