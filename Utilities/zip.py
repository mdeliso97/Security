import zipfile
import os


def zip_folder(folder_path):
    if os.path.isdir(folder_path):
        folder_name = os.path.basename(folder_path)
        with zipfile.ZipFile(folder_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # If it's a directory, add all files in the directory to the zip
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, os.path.join(os.path.basename(folder_path), arcname))

    return folder_name


