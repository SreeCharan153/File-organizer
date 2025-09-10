import os
import shutil
import json
import logging

with open("config.json") as f:
    CATEGORIES = json.load(f)

logging.basicConfig(filename="organizer.log", level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def get_category(ext):
    for category, exts in CATEGORIES.items():
        if ext.lower() in exts:
            return category
    return "Others"

def organize_files(directory):
    if not os.path.exists(directory):
        print("Folder does not exist.")
        return
    
    for category in CATEGORIES.keys():
        os.makedirs(os.path.join(directory, category), exist_ok=True)
        
    for file in os.listdir(directory):
        filepath = os.path.join(directory, file)
        if os.path.isfile(filepath):
            name, ext = os.path.splitext(file)
            category = get_category(ext)
            dest_path = os.path.join(directory, category, file)
            try:
                shutil.move(filepath, dest_path)
                logging.info(f"Moved: {file} -> {category}")
            except Exception as e:
                logging.error(f"Failed to move {file}: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
    print("Organizing complete. Check organizer.log for details.")
