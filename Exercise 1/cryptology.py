import tkinter as tk
from tkinter import filedialog
import pygame

from ECB import *
from CBC import *
from GCM import *
from RSA_OAEP import *


def open_file():
    global content
    global key

    file_path = filedialog.askopenfilename(
        title="Select a file", filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path and is_encrypt and not file_path.endswith(".json"):

        label3.config(text="Success: file to be encrypted uploaded!")
        with open(file_path, "rb") as file:
            content = file.read()
            # print content
            print("File content:\n", content)

    elif file_path.endswith(".json") and not is_encrypt.get() and (clicked0.get() == "CBC", "GCM"):
        # Read and process the .txt file
        label3.config(text="Success: file .json to be decrypted uploaded!")

        with open(file_path, "r") as file:
            content = file.read()
            # print content
            print("File content:\n", content)
    else:
        label3.config(text="Error: No file or wrong format was provided!")


def source_key():
    global key

    file_path = filedialog.askopenfilename(
        title="Select the key.txt file",
        filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path:
        # if file_path.endswith(".txt"):

        # Read and process the .txt file
        label3.config(text="Success: key uploaded successfully!")

        with open(file_path, "rb") as file:
            key = file.read()
            # print content
            print("File content:\n", key)
    else:
        label3.config(text="Error: selected file is not a file!")


def hide_option0():
    global is_sym

    if is_sym.get():
        drop1.pack_forget()
        drop0.pack(pady=10, after=checkbox1)
    else:
        drop0.pack_forget()
        drop1.pack(pady=10, after=checkbox1)


def hide_option1():
    if is_encrypt.get():
        button3.pack_forget()
    else:
        button3.pack(pady=20, before=button5, after=button2)


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


def start():
    global key
    global is_encrypt
    global is_sym

    if clicked0.get() == "ECB":

        if is_encrypt.get():
            message, key = ecb_encrypt(content)
            name_out = "ECB_encrypt"
        else:
            message = ecb_decrypt(content, key)
            name_out = "ECB_decrypt"

        print(message)

        # Write the result to a new text file in rb format (byte string)
        with open(f"{name_out}", "wb") as output_file:
            output_file.write(message)
            # label3.config(text="Success: result written to output.txt")

        if is_encrypt.get():
            with open("ECB_key", "wb") as output_file:
                output_file.write(key)
                label3.config(text=f"Success: encrypted file written to <{name_out}> and key to <ECB_key>")

    elif clicked0.get() == "CBC":
        if is_encrypt.get():
            message, key = encrypt_cbc(content)
            name_out = "CBC_encrypt"
        else:
            message = decrypt_cbc(content, key)
            name_out = "CBC_decrypt"

        # Write the result to a new text or json file
        if is_encrypt.get():
            with open(f"{name_out}.json", "w") as output_file:
                output_file.write(message)

            with open("CBC_key", "wb") as output_file:
                output_file.write(key)
                label3.config(text=f"Success: encrypted file written to <{name_out}> and key to <CBC_key>")

        else:
            with open(f"{name_out}", "wb") as output_file:
                output_file.write(message)
                label3.config(text=f"Success: decrypted file written to <{name_out}>")

    elif clicked0.get() == 'GCM':
        if is_encrypt.get():
            message, key = GCM_encryption(content)
            name_out = "GCM_encrypt"
        else:
            message = GCM_decryption(content, key)
            name_out = "GCM_decrypt"

        # Write the result to a new text or json file
        if is_encrypt.get():
            with open(f"{name_out}.json", "w") as output_file:
                output_file.write(message)

            with open("GCM_key", "wb") as output_file:
                output_file.write(key)
                label3.config(text=f"Success: encrypted file written to <{name_out}> and key to <GCM_key>")

        else:
            with open(f"{name_out}", "wb") as output_file:
                output_file.write(message)
                label3.config(text=f"Success: decrypted file written to <{name_out}>")

    elif clicked1.get() == 'RSA-OAEP':
        label3.config(text="Selected RSA-OAEP asymmetric cipher")

    else:
        if is_sym.get():
            label3.config(text="Select a cipher and/or upload the file before proceeding!")
        else:
            label3.config(text="Select a cipher and/or upload the encrypted file + key before proceeding!")


if __name__ == '__main__':
    # Initialize pygame
    pygame.mixer.init()

    global content
    global key

    root = tk.Tk()
    root.title("Crypto 8-bit")

    # Adjust size
    root.geometry("320x500")

    # datatype of menu text
    clicked0 = tk.StringVar()
    clicked1 = tk.StringVar()

    # initial menu text
    clicked0.set("Select Symmetric cipher")
    clicked1.set("Select Asymmetric cipher")

    # Create Dropdown menu
    drop0 = tk.OptionMenu(root, clicked0, *["Select Symmetric cipher", "ECB", "CBC", "GCM"])
    drop1 = tk.OptionMenu(root, clicked1, *["Select Asymmetric cipher", "RSA-OAEP"])

    label0 = tk.Label(root, text="Crypto 8-bit", font=("Helvetica", 24, "bold"), foreground="blue")
    label1 = tk.Label(root, text="Create your own key:", font=("Helvetica", 14, "bold"), foreground="black")
    label2 = tk.Label(root, text="TBD", font=("Helvetica", 14, "bold"), foreground="black")
    label3 = tk.Label(root, text="Welcome!", font=9, foreground="red")

    button2 = tk.Button(root, text="Source File", command=open_file)
    button3 = tk.Button(root, text="Source Key", command=source_key)
    button4 = tk.Button(root, text="Exit", command=on_closing)
    button5 = tk.Button(root, text="Start", command=start)

    is_sym = tk.BooleanVar()
    is_encrypt = tk.BooleanVar()
    checkbox0 = tk.Checkbutton(root, text="Checked sym. / Unchecked asym.", variable=is_sym,
                               command=hide_option0)
    checkbox1 = tk.Checkbutton(root, text="Checked encrypt. / Unchecked decrypt.", variable=is_encrypt,
                               command=hide_option1)
    label0.pack(pady=30)
    checkbox0.pack(pady=0)
    checkbox1.pack(pady=10)
    # drop0.pack(pady=10)
    drop1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=20)
    button5.pack(pady=10)
    button4.pack()
    label3.pack(pady=20)

    # Bind the exit event handler to the window's close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Bind with start button
    root.protocol("START", start)

    # Load and play the MP3 file
    pygame.mixer.music.load("jeremy_blake-powerup.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    root.mainloop()
