from pydub import AudioSegment


def convert(file_name):
    # Specify the output file path in the "model" folder
    output_path = f"model/output.wav"

    audio = AudioSegment.from_file(file_name)
    audio = (
        audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    )  # Set the desired audio properties

    audio.export(output_path, format="wav")
