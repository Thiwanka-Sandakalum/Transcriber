from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import os


def convert_audio_to_wav(
    input_file, output_file, frame_rate=16000, channels=1, sample_width=2
):
    audio = AudioSegment.from_file(input_file)

    # Set the desired audio properties
    audio = (
        audio.set_frame_rate(frame_rate)
        .set_channels(channels)
        .set_sample_width(sample_width)
    )

    # Export the audio to WAV format
    audio.export(output_file, format="wav")
    print("..............................................converted ")


def convert_video_to_wav(video_file, output_file, frame_rate=16000, channels=1, sample_width=2):
    # Load the video clip
    clip = VideoFileClip(video_file)

    try:
        # Extract the audio from the video
        audio = clip.audio

        # Export the audio as a temporary file in WAV format
        temp_wav_path = "temp.wav"
        audio.write_audiofile(temp_wav_path, codec="pcm_s16le")

        # Convert the temporary WAV file to the desired format
        convert_audio_to_wav(temp_wav_path, output_file, frame_rate, channels, sample_width)
    finally:
        # Close the video clip and remove the temporary WAV file
        clip.close()
        os.remove(temp_wav_path)
        os.remove(video_file)


if __name__ == "__main__":
    # Example usage
    video_path = "path/to/video.mp4"
    output_path = "model/output.wav"

    convert_video_to_wav(video_path, output_path)
