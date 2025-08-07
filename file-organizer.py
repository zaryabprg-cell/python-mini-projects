import os
import shutil

# Set the folder you want to organize
folder_path = input("Enter the path of the folder to organize: ")

# File type categories
file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Documents": ['.pdf', '.docx', '.txt', '.pptx'],
    "Music": ['.mp3', '.wav'],
    "Archives": ['.zip', '.rar', '.tar'],
    "Scripts": ['.py', '.js', '.html', '.css'],
    "Others": []
}

def create_folder(name):
    path = os.path.join(folder_path, name)
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def move_file(file, dest_folder):
    shutil.move(os.path.join(folder_path, file), os.path.join(dest_folder, file))

def get_category(file_ext):
    for category, extensions in file_types.items():
        if file_ext in extensions:
            return category
    return "Others"

def organize():
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            _, ext = os.path.splitext(file)
            category = get_category(ext.lower())
            dest_folder = create_folder(category)
            move_file(file, dest_folder)
            print(f"Moved: {file} → {category}/")

organize()
print("✅ Done organizing files!")
