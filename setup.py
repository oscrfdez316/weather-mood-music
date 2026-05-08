import os

# Create folder structure
folders = [
    'data/raw/spotify_real',
    'data/raw/weather_real',
    'data/processed',
    'results/figures',
    'report'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folder structure created successfully\n")
print("=" * 55)
print("NEXT STEPS: Download the following datasets from Kaggle")
print("=" * 55)
print()
print("1. Spotify Mood Dataset (Moodify):")
print("   https://www.kaggle.com/datasets/abdullahorzan/moodify-dataset")
print("   -> Click 'Download' on Kaggle (you need a free account)")
print("   -> You will get a zip file called archive.zip")
print("   -> Unzip it and place the CSV files inside: data/raw/spotify_real/")
print("   -> You should see: 278k_song_labelled.csv")
print()
print("2. Historical Hourly Weather Data:")
print("   https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data")
print("   -> Click 'Download' on Kaggle")
print("   -> You will get a zip file called archive.zip")
print("   -> Unzip it and place the CSV files inside: data/raw/weather_real/")
print("   -> You should see: temperature.csv, humidity.csv, weather_description.csv, city_attributes.csv")
print()
print("Once done, launch Jupyter and run notebooks 01 through 04 in order.")
print("=" * 55)
