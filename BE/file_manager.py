import os
import shutil

def save_to_folder(file, category_folder):
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)
    shutil.copy(file, os.path.join(category_folder, os.path.basename(file)))
