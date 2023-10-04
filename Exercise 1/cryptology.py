import tkinter as tk
from tkinter import filedialog
import functools
import pygame

import ECB
from ECB import *
from CBC import *
from AES_GCM import *
from RES import *


def open_file():
    global content
    global key

    file_path = filedialog.askopenfilename(
        title="Select a .txt file", filetypes=[("Text Files", "*.txt"), ("Json Files", "*.json"), ("All Files", "*.*")])  # Specify file types

    if file_path:
        if file_path.endswith(".txt"):
            # Read and process the .txt file
            label1.config(text="Success: file .txt uploaded successfully!")

            with open(file_path, "r") as file:
                content = file.read()
                # print content
                print("File content:\n", content)
        elif file_path.endswith(".json"):
            # Read and process the .txt file
            label1.config(text="Success: file .json uploaded successfully!")

            with open(file_path, "r") as file:
                content = file.read()
                # print content
                print("File content:\n", content)
        else:
            label1.config(text="Error: selected file is neither a .txt nor .json file!")


def source_key():
    global key_pub
    file_path = filedialog.askopenfilename(
        title="Select the key.txt file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])  # Specify file types

    if file_path:
        if file_path.endswith(".txt"):
            # Read and process the .txt file
            label1.config(text="Success: file .txt uploaded successfully!")

            with open(file_path, "r") as file:
                key_pub = file.read()
                # print content
                print("File content:\n", key)
        else:
            label1.config(text="Error: selected file is not a .txt file!")


def hide_option():
    if is_encrypt.get():
        button3.pack_forget()
    else:
        button3.pack(before=button5)


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


def start():
    global key
    global is_encrypt

    if key is None:
        key = 0

    if clicked0.get() == "ECB" and clicked1.get() == "RES":
        message, key = ECB.ecb_encrypt(content, is_encrypt, key)
        message, key = ECB.ecb_decrypt(content, is_encrypt, key)

        print(message)

        # Write the result to a new text file in rb format (byte string)
        with open("output", "w") as output_file:
            output_file.write(str(message))
            # label1.config(text="Success: result written to output.txt")

        with open("key", "w") as output_file:
            output_file.write(str(key))
            label1.config(text="Success: encrypted file written to <output> and key to <key>")

    elif clicked0.get() == "CBC" and clicked1.get() == "RES":
        message, key = cbc(content, is_encrypt)

        # Write the result to a new text or json file
        if is_encrypt:
            with open("output", "w") as output_file:
                output_file.write(message)

            with open("key", "w") as output_file:
                output_file.write(key)
                label1.config(text="Success: encrypted file written to <output> and key to <key>")

        else:
            with open("output", "w") as output_file:
                output_file.write(message)
                label1.config(text="Success: decrypted file written to <output>")


if __name__ == '__main__':
    # Initialize pygame
    pygame.mixer.init()

    global content
    global key_pub

    key = None

    root = tk.Tk()
    root.title("Crypto 8-bit")

    # Define a custom font and foreground color for the title
    title_font = ("Helvetica", 24, "bold")  # Change the font family, size, and style
    title_color = "blue"  # Change the text color

    # Adjust size
    root.geometry("300x450")

    # datatype of menu text
    clicked0 = tk.StringVar()
    clicked1 = tk.StringVar()

    # initial menu text
    clicked0.set("Select Symmetric cypher")
    clicked1.set("Select Asymmetric cypher")

    # Create Dropdown menu
    drop0 = tk.OptionMenu(root, clicked0, *["ECB", "CBC", "AES-GCM"])
    drop1 = tk.OptionMenu(root, clicked1, *["RES"])

    label0 = tk.Label(root, text="Crypto 8-bit", font=title_font, foreground=title_color)
    label1 = tk.Label(root, text="Welcome!", font=11, foreground="red")

    button2 = tk.Button(root, text="Source File", command=open_file)
    button3 = tk.Button(root, text="Source Key", command=source_key)
    button4 = tk.Button(root, text="Exit", command=on_closing)
    button5 = tk.Button(root, text="Start", command=start)

    is_encrypt = tk.BooleanVar()
    checkbox0 = tk.Checkbutton(root, text="Checked encrypt. / Unchecked decrypt.", variable=is_encrypt,
                               command=hide_option)
    label0.pack(pady=20)
    drop0.pack(pady=10)
    drop1.pack(pady=10)
    checkbox0.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=20)
    button5.pack(pady=10)
    button4.pack(pady=20)
    label1.pack(pady=10)

    # Bind the exit event handler to the window's close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Bind with start button
    root.protocol("START", start)

    # Load and play the MP3 file
    pygame.mixer.music.load("jeremy_blake-powerup.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    root.mainloop()
