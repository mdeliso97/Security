import tkinter as tk
import pygame

from tkinter import filedialog
from RSA_keygen import *
from ECB import *
from CBC import *
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

    elif file_path.endswith(".json") and not is_encrypt.get() and (clicked_sym.get() == "CBC", "GCM", "RSA-OAEP"):
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


def source_public_key():
    global key_public

    file_path = filedialog.askopenfilename(
        title="Select the key.txt file",
        filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path and file_path.endswith(".json"):
        # if file_path.endswith(".txt"):

        # Read and process the .txt file
        label3.config(text="Success: key uploaded successfully!")

        with open(file_path, "r") as file:
            key_public = file.read()
            # print content
            print("File content:\n", key_public)
    else:
        label3.config(text="Error: selected file is not a .json file!")


def source_private_key():
    global key_private

    file_path = filedialog.askopenfilename(
        title="Select the key file",
        filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path and file_path.endswith(".json"):

        with open(file_path, "r") as file:
            key_private = file.read()
            # print content
            print("File content:\n", key_private)

        # Read and process the .txt file
        label3.config(text="Success: private key uploaded successfully!")

    else:
        label3.config(text="Error: selected file is not a .json file!")


def hide_option():
    global is_sym
    global is_encrypt

    if is_encrypt.get() and is_sym.get():
        button_public.pack_forget()
        button_private.pack_forget()
        button_key.pack_forget()
        button_keygen.pack_forget()
        drop_asym.pack_forget()
        drop_sym.pack(pady=10, after=checkbox_encryption)
    elif not is_encrypt.get() and is_sym.get():
        button_public.pack_forget()
        button_private.pack_forget()
        button_key.pack(pady=5, after=button_file)
        button_keygen.pack_forget()
        drop_asym.pack_forget()
        drop_sym.pack(pady=10, after=checkbox_encryption)
    elif is_encrypt.get() and not is_sym.get():
        button_private.pack_forget()
        button_key.pack_forget()
        drop_sym.pack_forget()
        button_keygen.pack_forget()
        drop_asym.pack(pady=10, after=checkbox_encryption)
        button_keygen.pack(pady=10, before=drop_asym)
        button_public.pack(pady=5, after=button_file)
    elif not is_encrypt.get() and not is_sym.get():
        button_public.pack_forget()
        drop_sym.pack_forget()
        drop_asym.pack(pady=10, after=checkbox_encryption)
        button_keygen.pack(pady=10, before=drop_asym)
        button_key.pack(pady=5, after=button_file)
        button_private.pack(pady=5, after=button_key)


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


def keygen_output(json_output_public, json_output_private):
    with open("public_key.json", "w") as output_file:
        output_file.write(json_output_public)

    with open("private_key.json", "w") as output_file:
        output_file.write(json_output_private)


def start():
    global key
    global is_encrypt
    global is_sym
    global key_public

    if clicked_sym.get() == "ECB" and clicked_asym.get() == "Select Asymmetric cipher":

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

    elif clicked_sym.get() == "CBC" and clicked_asym.get() == "Select Asymmetric cipher":
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

    elif clicked_sym.get() == 'GCM' and clicked_asym.get() == "Select Asymmetric cipher":
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

    elif clicked_asym.get() == 'RSA-OAEP':
        if not is_sym.get():
            if is_encrypt.get():
                message, key = rsa_oaep_encryption(content, key_public)
                name_out = "RSA-OAEP_encrypt"
            else:
                message = rsa_oaep_decryption(content, key, key_private)
                name_out = "RSA-OAEP_decrypt"

            # Write the result to a new text or json file
            if is_encrypt.get():
                with open(f"{name_out}.json", "w") as output_file:
                    output_file.write(message)

                with open("RSA_key", "wb") as output_file:
                    output_file.write(key)
                    label3.config(
                        text=f"Success: encrypted file written to <{name_out}> and encrypted key to <RSA_key>")

            else:
                with open(f"{name_out}", "wb") as output_file:
                    output_file.write(message)
                    label3.config(text=f"Success: decrypted file written to <{name_out}>")

    else:
        if is_sym.get() and is_encrypt.get():
            label3.config(text="Select a cipher and/or upload the file before proceeding!")
        else:
            label3.config(text="Select a cipher and/or upload the encrypted file + key before proceeding!")


if __name__ == '__main__':
    # Initialize pygame
    pygame.mixer.init()

    global key_public
    global key_private
    global content
    global key

    root = tk.Tk()
    root.title("Crypto 8-bit")

    # Adjust size
    root.geometry("320x500")

    # datatype of menu text
    clicked_sym = tk.StringVar()
    clicked_asym = tk.StringVar()

    # initial menu text
    clicked_sym.set("Select Symmetric cipher")
    clicked_asym.set("Select Asymmetric cipher")

    # Create Dropdown menu
    drop_sym = tk.OptionMenu(root, clicked_sym, *["Select Symmetric cipher", "ECB", "CBC", "GCM"])
    drop_asym = tk.OptionMenu(root, clicked_asym, *["Select Asymmetric cipher", "RSA-OAEP"])

    label0 = tk.Label(root, text="Crypto 8-bit", font=("Helvetica", 24, "bold"), foreground="blue")
    label1 = tk.Label(root, text="Create your own key:", font=("Helvetica", 14, "bold"), foreground="black")
    label2 = tk.Label(root, text="TBD", font=("Helvetica", 14, "bold"), foreground="black")
    label3 = tk.Label(root, text="Welcome!", font=9, foreground="red")

    button_file = tk.Button(root, text="Source File", command=open_file)
    button_key = tk.Button(root, text="Source Key", command=source_key)
    button_exit = tk.Button(root, text="Exit", command=on_closing)
    button_start = tk.Button(root, text="Start", command=start)
    button_public = tk.Button(root, text="Source Public Key", command=source_public_key)
    button_private = tk.Button(root, text="Source Private Key", command=source_private_key)
    button_keygen = tk.Button(root, text="Keygen", command=keygen)

    is_sym = tk.BooleanVar()
    is_encrypt = tk.BooleanVar()
    checkbox_symmetric = tk.Checkbutton(root, text="Checked sym. / Unchecked asym.", variable=is_sym,
                                        command=hide_option)
    checkbox_encryption = tk.Checkbutton(root, text="Checked encrypt. / Unchecked decrypt.", variable=is_encrypt,
                                         command=hide_option)
    label0.pack(pady=30)
    checkbox_symmetric.pack(pady=0)
    checkbox_encryption.pack(pady=0)
    button_keygen.pack(pady=10)
    drop_asym.pack(pady=10)
    button_file.pack(pady=5)
    button_key.pack(pady=5)
    button_private.pack(pady=5)
    button_start.pack(pady=10)
    button_exit.pack()
    label3.pack(pady=20)

    # Bind the exit event handler to the window's close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Bind with start button
    root.protocol("START", start)

    # Load and play the MP3 file
    pygame.mixer.music.load("jeremy_blake-powerup.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    root.mainloop()
