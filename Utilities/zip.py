import shutil
import zipfile
import os
from tkinter import messagebox


def zip_file(folder_path):
    if os.path.isdir(folder_path):
        # folder_name = os.path.basename(folder_path)
        with zipfile.ZipFile(folder_path + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
            # If it's a directory, add all files in the directory to the zip
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, os.path.join(os.path.basename(folder_path), arcname))

        # Ask the user for confirmation
        confirmation = messagebox.askyesno("Confirmation", "Do you want to delete the previous directory?")

        if confirmation:
            # Delete the previous directory
            try:
                shutil.rmtree(folder_path)
                messagebox.showinfo("Information", "Directory deleted successfully.")
            except OSError as e:
                messagebox.showerror("Error", f"Error deleting directory: {str(e)}")

        return folder_path + ".zip"


def unzip_file(file, output_path):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(output_path)

    # Delete the zip file
    os.remove(file)
