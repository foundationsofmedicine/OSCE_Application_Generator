import os
import shutil

def copypublic(from_path, to_path):

    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)