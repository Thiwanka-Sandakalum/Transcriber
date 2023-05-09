# Copyright (C) 2023 Thiwanka Sandakalum. All rights reserved.
# Developed by Thiwanka Sandakalum

from youtube_down import download_audio_from_youtube
from pod_down import PodcastDownloader
from converter import convert_video_to_wav, convert_audio_to_wav
import os
import Transcriber

output_path = "model/output.wav"


def get_user_input(message, valid_inputs):
    while True:
        user_input = input(message).strip().upper()
        if user_input in valid_inputs:
            return user_input
        print("Invalid input. Please try again.")


def download_and_transcribe():
    user_input_1 = get_user_input(
        "If you want to transcribe press T or if you want to summarize press S: ",
        ["T", "S"],
    )

    user_input_2 = get_user_input(
        "For YouTube press Y\n"
        "For Google Podcast press P\n"
        "For video or audio file press F\n",
        ["Y", "P", "F"],
    )

    if user_input_2 == "Y":
        url = input("Enter YouTube URL: ")
        download_audio_from_youtube(url)

    elif user_input_2 == "P":
        url = input("Enter Podcast URL: ")
        PodcastDownloader(url)

    else:
        print(" 1 : File type: mp4")
        print(" 2 : File type: mp3")

        in_fl = input("Insert Number: ")
        input_file = input("Insert path for file: ")

        if in_fl == "1":
            os.rename(input_file, "output.mp4")
            convert_video_to_wav(video_file="output.mp4", output_file=output_path)

        elif in_fl == "2":
            os.rename(input_file, "output.mp3")
            convert_audio_to_wav(input_file="output.mp3", output_file=output_path)

    if user_input_1 == "T":
        Transcriber.build_command()
    else:
        # Implement summarize_audio function here
        pass

    # Clean up temporary audio file
    file_paths = ["output.wav", "output.mp4", "output.mp3"]

    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    download_and_transcribe()
