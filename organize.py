import os
import shutil

# Target directory to organize
TARGET_DIR = './target_folder'  # Change as needed

FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv'],
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return 'Others'

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            category = get_category(filename)
            category_dir = os.path.join(directory, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
            shutil.move(file_path, os.path.join(category_dir, filename))

if __name__ == "__main__":
    organize_files(TARGET_DIR)
    print("Files organized successfully.")
