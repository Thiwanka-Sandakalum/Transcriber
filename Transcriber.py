import os

FILE_TYPES = {
    1: "-otxt",
    2: "-ovtt",
    3: "-osrt",
    4: "-olrc",
    5: "-ocsv",
    6: "-oj",
}


def run_process(output_type):
    try:
        # Change directory to the model folder
        os.chdir("./model")

        # Command to run
        command = f"./main -m ggml-tiny.bin -f output.wav {output_type} -of ./output/output"

        # Run the command
        os.system(command)
    except OSError as error:
        print(f"Error: {error}")


def output(ftype):
    return FILE_TYPES.get(ftype, "-otxt")


def build_command():
    file_type_menu = (
        "1 : Output result in a text file\n"
        "2 : Output result in a vtt file\n"
        "3 : Output result in a srt file\n"
        "4 : Output result in a lrc file\n"
        "5 : Output result in a CSV file\n"
        "6 : Output result in a JSON file\n"
    )
    print(file_type_menu)

    while True:
        ftype = input("Please insert file type (1-6): ")
        if ftype.isdigit() and 1 <= int(ftype) <= 6:
            output_type = output(int(ftype))
            run_process(output_type)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    build_command()
