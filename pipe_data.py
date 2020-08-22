import os
import pandas as pd

csv_path = r"C:\Users\Jayee Li\Desktop\torch\dataset.csv"
dataset = pd.read_csv(csv_path)

print("adding data entries.")
audio_directory = r"C:\Users\Jayee Li\Desktop\torch\audio"
text_directory = r"C:\Users\Jayee Li\Desktop\torch\texts"

#look through all files in both data directories
for audio_filename in os.listdir(audio_directory):
    for text_filename in os.listdir(text_directory):
        if os.path.splitext(audio_filename)[0] == os.path.splitext(text_filename)[0]:
            audio_filepath = os.path.join(audio_directory, audio_filename)
            text_filepath = os.path.join(text_directory, text_filename)

            if audio_filepath in dataset.audio.values:
                print(audio_filepath)
                print("already exists!")
            else:
                entry = pd.DataFrame([[audio_filepath, text_filepath]],columns=['audio','texts'])
                dataset = dataset.append(entry, ignore_index=True)

#write dataframe to csv
print(dataset)
dataset.to_csv(csv_path, index=False)
print("finished adding new data entries.")
