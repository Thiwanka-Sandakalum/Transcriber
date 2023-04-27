import whisper

def transcribe_audio(model_name, file_path):
    # load the specified model
    model = whisper.load_model(model_name)
    
    # transcribe the audio file using the model
    result = model.transcribe(file_path)
    text = result["text"]
    
    # write the transcribed text to a file
    with open("output.txt", "w") as f:
        f.write(text)
