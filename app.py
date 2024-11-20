import whisper
import os
import librosa  # You'll need this if your audio files aren't all WAV

model = whisper.load_model("base")  # Or another size

audio_dir = "audio"  # Replace with the directory containing your audio files
output_dir = "output" # Replace with desired directory for text output

os.makedirs(output_dir, exist_ok=True) # creates output dir, if it doesn't exist


for filename in os.listdir(audio_dir):
    if filename.endswith((".wav", ".mp3", ".m4a", ".ogg")):  # Add other extensions as needed
        file_path = os.path.join(audio_dir, filename)

        try:
            # Load audio – handles different formats gracefully
            audio, sr = librosa.load(file_path, sr=16000)  # librosa resamples if needed

            result = model.transcribe(audio)
            text = result["text"]


            output_filename = os.path.splitext(filename)[0] + ".txt"  # Name output file after the audio file
            output_file_path = os.path.join(output_dir, output_filename)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Transcribed {filename} to {output_filename}")


        except Exception as e:
            print(f"Error transcribing {filename}: {e}")