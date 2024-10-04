from os import listdir
from os.path import isfile, join
import os
import shutil

file_path = r'C:\Users\Files'
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

categories = {
    'pictures': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv'],
    'pdfs': ['pdf'],
    'documents': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt'],
    'audio': ['mp3', 'wav', 'aac', 'flac'],
    'archives': ['zip', 'rar', '7z', 'tar', 'gz'],
}

category_folders = {}

for category in categories:
    new_folder_name = os.path.join(file_path, category + '_folder')
    category_folders[category] = new_folder_name
    if not os.path.exists(new_folder_name):
        os.mkdir(new_folder_name)

v = 1
for file in files:
    filetype = file.split('.')[-1].lower()
    moved = False
    for category, extensions in categories.items():
        if filetype in extensions:
            src_path = os.path.join(file_path, file)
            dest_path = category_folders[category]
            shutil.move(src_path, dest_path)
            print(v, '. ', src_path + ' >>> ' + dest_path)
            v += 1
            moved = True
            break
    if not moved:
        others_folder = os.path.join(file_path, 'others_folder')
        if not os.path.exists(others_folder):
            os.mkdir(others_folder)
        src_path = os.path.join(file_path, file)
        shutil.move(src_path, others_folder)
        print(v, '. ', src_path + ' >>> ' + others_folder)
        v += 1
