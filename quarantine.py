import os
import json
import shutil

# Define the source folder containing JSON files
source_folder = "Projekt\corpus_finished_new"

# Define the quarantine folder where empty "poem" files will be moved
quarantine_folder = "Projekt\quarantine"

# Ensure the quarantine folder exists; create it if it doesn't
if not os.path.exists(quarantine_folder):
    os.makedirs(quarantine_folder)

# Iterate over each file in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a JSON file
    if filename.endswith(".json"):
        # Construct the full file path
        file_path = os.path.join(source_folder, filename)

        # Read the JSON file
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

            # Check if the "poem" field is empty
            if not data.get("poem"):
                # Move the file to the quarantine folder
                shutil.move(file_path, os.path.join(quarantine_folder, filename))

# Print a message when the operation is complete
print("Operation completed.")
