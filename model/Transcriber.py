import os
import requests


url = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.bin"
output_file = "ggml-tiny.bin"


def model_download():
    if os.path.exists(output_file):
        print(f"Model '{output_file}' already exists in the directory.")
    else:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, "wb") as file:
                file.write(response.content)
            print(f"Model downloaded and saved as '{output_file}'.")
        else:
            print("Failed to download the model.")


def run_process(output_type):
    command = f"./main -m ggml-tiny.bin -f , output.wav {output_type} "
    try:
        os.system(command)
    except OSError as error:
        print(f"Error: {error}")


def output(ftype):
    ftype = int(ftype)
    if ftype == 1:
        return "-otxt"
    elif ftype == 2:
        return "-ovtt"
    elif ftype == 3:
        return "-osrt"
    elif ftype == 4:
        return "-olrc"
    elif ftype == 5:
        return "-ocsv"
    elif ftype == 6:
        return "-oj"


def build_command():
    print(
        "1 : Output result in a text file\n"
        "2 : Output result in a vtt file\n"
        "3 : Output result in a srt file\n"
        "4 : Output result in a lrc file\n"
        "5 : Output result in a CSV file\n"
        "6 : Output result in a JSON file\n"
    )

    while True:
        ftype = input("Please insert file type (1-6): ")
        if ftype.isdigit() and 1 <= int(ftype) <= 6:
            output_type = output(ftype)
            print(output_type)
            model_download()
            run_process(output_type)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")


build_command()
