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
print("   -> Place CSV files in: data/raw/spotify_real/")
print()
print("2. Historical Hourly Weather Data:")
print("   https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data")
print("   -> Place CSV files in: data/raw/weather_real/")
print()
print("Once done, launch Jupyter and run notebooks 01 through 04 in order.")
print("=" * 55)
