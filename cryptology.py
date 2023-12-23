import tkinter as tk
import pygame
import os

from Utilities import keygen
from tkinter import filedialog, messagebox
from Ciphers.ECB import ecb_encrypt, ecb_decrypt
from Ciphers.CBC import cbc_encrypt, cbc_decrypt
from Ciphers.GCM import gcm_encrypt, gcm_decrypt
from Ciphers.RSA_OAEP import rsa_oaep_encryption, rsa_oaep_decryption
from Ciphers.RSA import rsa_encryption, rsa_decryption
from Utilities.dialog_message import dialog_message
from Utilities.zip import zip_file, unzip_file

'''
This class is the main of Crypto 8-bit, defines all the GUI elements and initiates them, handles all different ciphers
and defines uploading of files when required for specific action. The program is able to encrypt and decrypt whatever
file is given as input and comes with different ciphers that can be applied: ECM, CBC, GCM AEAD, RSA and RSA-OAEP (still
in progress).
'''


# changes the name of source button dynamically
def update_button_source():
    global is_not_directory

    new_text = "Source File" if is_not_directory.get() else "Source Directory"
    button_file.config(text=new_text)


# allows printing new text in the widget console by unlocking and locking console state
def widget_console(new_text):
    text_widget0.config(state=tk.NORMAL)
    text_widget0.delete(1.0, "end-1c")
    text_widget0.insert("1.0", new_text)
    text_widget0.config(state=tk.DISABLED)


# allows to enter own key for encryption and decryption, handles exceptions and avoids not good passwords
def widget_password():
    global password

    password = None

    if len(text_widget1.get()) < 8 and len(text_widget1.get()) % 4 == 0:
        widget_console("Error: No valid password, please make sure it is at least 8 characters or numbers")
    elif len(text_widget1.get()) % 4 != 0 and not len(text_widget1.get()) < 8:
        widget_console("Error: No valid password, please make sure the password length is a multiple of 4")

    elif len(text_widget1.get()) < 8 and len(text_widget1.get()) % 4 != 0:
        widget_console("Error: No valid password, please make sure it is at least 8 characters or numbers "
                       "and the length is a multiple of 4")
    else:
        text_widget1.config(state=tk.DISABLED)
        widget_console("Success: password will be used for encryption/decryption")
        password = text_widget1.get()
        button_key.pack_forget()


# makes sure after encryption or decryption the password widget is active and empty again
def widget_password_reset():
    global password

    password = None
    text_widget1.config(state=tk.NORMAL)
    text_widget1.delete(0, tk.END)


def popup_description():
    info = dialog_message()
    messagebox.showinfo("Instructions", info)


# executes keygen for private and public key creation
def keygen_exe():
    keygen.keygen()
    widget_console("Success: private key <private_key.json> and public key <public_key.json> generated!")


# defines logic to source a file and handles wrong behaviors related to the selection of the file
def open_file():
    global content
    global key
    global file_extension
    global filename
    global is_not_directory

    if not is_not_directory.get():
        file_path = filedialog.askdirectory(title="Select a directory")  # Specify directory
        file_path = zip_file(file_path)

    else:
        file_path = filedialog.askopenfilename(
            title="Select a file", filetypes=[("All Files", "*.*")])  # Specify file

    if is_encrypt.get():
        filename = os.path.splitext(os.path.basename(file_path))[0]
        file_extension = os.path.splitext(os.path.basename(file_path))[1]

    if file_path:
        if is_encrypt.get() and not file_path.endswith(".json"):
            if not is_not_directory.get():
                widget_console(f"A zipped copy of your folder {file_path} has been generated for encryption")
            else:
                widget_console("Success: file to be encrypted uploaded!")

            with open(file_path, "rb") as file:
                content = file.read()

        elif not is_not_directory.get() and not is_encrypt.get() and (
                clicked_sym.get() == "ECB", "CBC", "GCM", "RSA", "RSA-OAEP") and file_path.endswith(".json"):

            widget_console("Success: file .json to be decrypted uploaded!")

            with open(file_path, "r") as file:
                content = file.read()
        else:
            widget_console("Error: Wrong file format was provided!")
    else:
        widget_console("Error: No file provided!")


# defines logic to source a key and handles wrong behaviors related to the selection of the key
def source_key():
    global key

    file_path = filedialog.askopenfilename(
        title="Select the key.txt file",
        filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path:
        widget_console("Success: key uploaded successfully!")

        text_widget1.pack_forget()
        button_password.pack_forget()
        frame_password.pack_forget()

        with open(file_path, "rb") as file:
            key = file.read()
    else:
        widget_console("Error: selected file is not a file!")


# defines logic to source a public key and handles wrong behaviors related to the selection of the public key
def source_public_key():
    global key_public

    file_path = filedialog.askopenfilename(
        title="Select the key.txt file",
        filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path and file_path.endswith(".json"):
        widget_console("Success: public key uploaded successfully!")

        with open(file_path, "r") as file:
            key_public = file.read()
    else:
        widget_console("Error: selected file is not a .json file!")


# defines logic to source a private key and handles wrong behaviors related to the selection of the private key
def source_private_key():
    global key_private

    file_path = filedialog.askopenfilename(
        title="Select the key file",
        filetypes=[("All Files", "*.*")])  # Specify file types

    if file_path and file_path.endswith(".json"):

        with open(file_path, "r") as file:
            key_private = file.read()

        # Read and process the .txt file
        widget_console("Success: private key uploaded successfully!")

    else:
        widget_console("Error: selected file is not a .json file!")


# defines which buttons or menus should be shown at specific conditions
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
        frame_password.pack(after=checkbox_encryption)
        text_widget1.pack(side=tk.LEFT, padx=10)
        button_password.pack(side=tk.RIGHT, padx=10)
    elif not is_encrypt.get() and is_sym.get():
        button_public.pack_forget()
        button_private.pack_forget()
        button_keygen.pack_forget()
        drop_asym.pack_forget()
        button_key.pack(pady=5, after=frame_search_type)
        drop_sym.pack(pady=10, after=checkbox_encryption)
        frame_password.pack(after=checkbox_encryption, pady=10)
        text_widget1.pack(side=tk.LEFT, padx=10)
        button_password.pack(side=tk.RIGHT, padx=10)
    elif is_encrypt.get() and not is_sym.get():
        button_private.pack_forget()
        button_key.pack_forget()
        drop_sym.pack_forget()
        button_keygen.pack_forget()
        text_widget1.pack_forget()
        button_password.pack_forget()
        frame_password.pack_forget()
        drop_asym.pack(pady=10, after=checkbox_encryption)
        button_keygen.pack(pady=10, before=drop_asym)
        button_public.pack(pady=5, after=frame_search_type)
    elif not is_encrypt.get() and not is_sym.get():
        button_public.pack_forget()
        drop_sym.pack_forget()
        text_widget1.pack_forget()
        button_password.pack_forget()
        frame_password.pack_forget()
        drop_asym.pack(pady=10, after=checkbox_encryption)
        button_keygen.pack(pady=10, before=drop_asym)
        button_key.pack(pady=5, after=frame_search_type)
        button_private.pack(pady=5, after=button_key)


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


# toggles on/off the volume
def volume_toggler():
    global is_volume_on
    is_volume_on = not is_volume_on
    if is_volume_on:
        button_volume.configure(image=volume_on)
        pygame.mixer.music.unpause()
    else:
        button_volume.configure(image=volume_off)
        pygame.mixer.music.pause()


# Defines actions when pressing start button
def start():
    global key
    global is_encrypt
    global is_sym
    global key_public
    global password
    global extension

    try:
        # creates a Results folder if it does not exist, otherwise it enters the folder
        if os.path.exists("Results"):
            os.chdir("Results")
        else:
            os.makedirs("Results")
            os.chdir("Results")

        # ECB cipher handler
        if clicked_sym.get() == "ECB" and clicked_asym.get() == "Select Asymmetric cipher":

            if is_encrypt.get():
                if password is not None:
                    message = ecb_encrypt(content, password, filename, file_extension)
                    name_out = f"{filename}_ECB_encrypt"
                else:
                    message, key = ecb_encrypt(content, password, filename, file_extension)
                    name_out = f"{filename}_ECB_encrypt"
            else:
                if password is not None:
                    message, filename_dec, extension = ecb_decrypt(content, password)
                    name_out = f"{filename_dec}_ECB_decrypt"
                else:
                    message, filename_dec, extension = ecb_decrypt(content, key)
                    name_out = f"{filename_dec}_ECB_decrypt"

            # Write the result to a new text file in rb format (byte string)
            if is_encrypt.get():
                with open(f"{name_out}.json", "w") as output_file:
                    output_file.write(message)
                if password is None:
                    with open(f"{filename}_ECB_key", "wb") as output_file:
                        output_file.write(key)
                        widget_console(
                            f"Success: encrypted file written to <{name_out}.json> and key to <{filename}_ECB_key> in Results folder")
                else:
                    widget_console(f"Success: encrypted file written to <{name_out}.json> in Results folder")

            else:
                with open(f"{name_out}{extension}", "wb") as output_file:
                    output_file.write(message)
                widget_console(f"Success: decrypted file written to <{name_out}> in Results folder")

            widget_password_reset()

        # CBC cipher handler
        elif clicked_sym.get() == "CBC" and clicked_asym.get() == "Select Asymmetric cipher":
            if is_encrypt.get():
                if password is not None:
                    message = cbc_encrypt(content, password, filename, file_extension)
                    name_out = f"{filename}_CBC_encrypt"
                else:
                    message, key = cbc_encrypt(content, password, filename, file_extension)
                    name_out = f"{filename}_CBC_encrypt"
            else:
                if password is not None:
                    message, filename_dec, extension = cbc_decrypt(content, password)
                    name_out = f"{filename_dec}_CBC_decrypt"
                else:
                    message, filename_dec, extension = cbc_decrypt(content, key)
                    name_out = f"{filename_dec}_CBC_decrypt"

            # Write the result to a new text or json file
            if is_encrypt.get():
                with open(f"{name_out}.json", "w") as output_file:
                    output_file.write(message)

                if password is None:
                    with open(f"{filename}_CBC_key", "wb") as output_file:
                        output_file.write(key)
                        widget_console(
                            f"Success: encrypted file written to <{name_out}.json> and key to <{filename}_CBC_key> in Results folder")
                else:
                    widget_console(f"Success: encrypted file written to <{name_out}.json> in Results folder")

            else:
                with open(f"{name_out}{extension}", "wb") as output_file:
                    output_file.write(message)
                    widget_console(f"Success: decrypted file written to <{name_out}> in Results folder")

            widget_password_reset()

        # GCM cipher handler
        elif clicked_sym.get() == 'GCM' and clicked_asym.get() == "Select Asymmetric cipher":
            if is_encrypt.get():
                if password is not None:
                    message = gcm_encrypt(content, password, filename, file_extension)
                    name_out = f"{filename}_GCM_encrypt"
                else:
                    message, key = gcm_encrypt(content, password, filename, file_extension)
                    name_out = f"{filename}_GCM_encrypt"
            else:
                if password is not None:
                    message, filename_dec, extension = gcm_decrypt(content, password)
                    name_out = f"{filename_dec}_GCM_decrypt"
                else:
                    message, filename_dec, extension = gcm_decrypt(content, key)
                    name_out = f"{filename_dec}_GCM_decrypt"

            # Write the result to a new text or json file
            if is_encrypt.get():
                with open(f"{name_out}.json", "w") as output_file:
                    output_file.write(message)

                if password is None:
                    with open(f"{filename}_GCM_key", "wb") as output_file:
                        output_file.write(key)
                        widget_console(
                            f"Success: encrypted file written to <{name_out}.json> and key to <{filename}_GCM_key> in Results folder")
                else:
                    widget_console(f"Success: encrypted file written to <{name_out}.json> in Results folder")

            else:
                with open(f"{name_out}{extension}", "wb") as output_file:

                    output_file.write(message)

                if extension == ".zip":
                    unzip_file(f"{name_out}{extension}", os.getcwd())

                widget_console(f"Success: decrypted file written to <{name_out}> in Results folder")

            widget_password_reset()

        elif clicked_asym.get() == 'RSA' and clicked_sym.get() == 'GCM':
            if not is_sym.get():
                if is_encrypt.get():
                    message, key = rsa_encryption(content, key_public, filename, file_extension)
                    name_out = f"{filename}_RSA_encrypt"
                else:
                    message, filename_dec, extension = rsa_decryption(content, key, key_private)
                    name_out = f"{filename_dec}_RSA_decrypt"

                # Write the result to a new text or json file
                if is_encrypt.get():
                    with open(f"{name_out}.json", "w") as output_file:
                        output_file.write(message)

                    with open(f"{filename}_RSA_key", "w") as output_file:
                        output_file.write(str(key))
                        widget_console(
                            f"Success: encrypted file written to <{name_out}.json> and encrypted key to <{filename}_RSA_key> in Results folder")

                else:
                    with open(f"{name_out}{extension}", "wb") as output_file:
                        output_file.write(message)
                        widget_console(f"Success: decrypted file written to <{name_out}> in Results folder")

            else:
                widget_console(
                    "Error: You cannot perform sym. while selecting an asym. cipher, please deselect"
                    " the asym. cipher if you aim to perform a sym. encryption/decryption or check the asym. checkbox!")

            widget_password_reset()

        elif clicked_asym.get() == 'RSA-OAEP' and clicked_sym.get() == 'GCM':
            if not is_sym.get():
                if is_encrypt.get():
                    message, key = rsa_oaep_encryption(content, key_public, filename, file_extension)
                    name_out = f"{filename}_RSA-OAEP_encrypt"
                else:
                    message, filename_dec, extension = rsa_oaep_decryption(content, key, key_private)
                    name_out = f"{filename_dec}_RSA-OAEP_decrypt"

                # Write the result to a new text or json file
                if is_encrypt.get():
                    with open(f"{name_out}.json", "w") as output_file:
                        output_file.write(message)

                    with open(f"{filename}_RSA-OAEP_key", "w") as output_file:
                        output_file.write(str(key))
                        widget_console(
                            f"Success: encrypted file written to <{name_out}.json> and encrypted key to <{filename}_RSA-OAEP_key> in Results folder")

                else:
                    with open(f"{name_out}{extension}", "wb") as output_file:
                        output_file.write(message)
                        widget_console(f"Success: decrypted file written to <{name_out}> in Results folder")

            else:
                widget_console(
                    "Error: You cannot perform sym. while selecting an asym. cipher, please deselect"
                    " the asym. cipher if you aim to perform a sym. encryption/decryption or check the asym. checkbox!")

            widget_password_reset()

        # wrong events handlers
        else:
            if is_sym.get() and is_encrypt.get():
                widget_console("Error: Select ONLY a symmetric cipher and upload the file before proceeding!")

            elif not is_sym.get() and is_encrypt.get():
                widget_console(
                    "Error: Select an AEAD symmetric cipher, an asymmetric cipher and upload the file and public key"
                    " before proceeding!")

            elif is_sym.get() and not is_encrypt.get():
                widget_console(
                    "Error: Select a symmetric cipher and upload the key and encrypted file you want to decrypt"
                    " before proceeding!")

            elif not is_sym.get() and not is_encrypt.get():
                widget_console(
                    "Error: Select an AEAD sym + asym. cipher and upload the encrypted file you want to decrypt, "
                    "the encrypted key and the private key before proceeding!")
        os.chdir(parent_directory)
    except Exception:
        os.chdir(parent_directory)
        return widget_console("Error: you are trying to use the program in the wrong way, please read the instructions "
                              "by selecting the button on the upper right corner.")


if __name__ == '__main__':
    key_public = None
    key_private = None
    content = None
    key = None
    password = None
    is_volume_on = True
    file_extension = None
    extension = None
    filename = None

    parent_directory = os.getcwd()

    # Initialize pygame
    pygame.mixer.init()

    # initialize TK object
    root = tk.Tk()
    root.title("Crypto 8-bit")

    # adjust size of GUI
    root.geometry("320x580")

    # datatype of different objects
    clicked_sym = tk.StringVar()
    clicked_asym = tk.StringVar()
    is_sym = tk.BooleanVar()
    is_encrypt = tk.BooleanVar()
    is_not_directory = tk.BooleanVar(value=True)

    # initial drop down menus text
    clicked_sym.set("Select Symmetric cipher")
    clicked_asym.set("Select Asymmetric cipher")

    # create Dropdown menu
    drop_sym = tk.OptionMenu(root, clicked_sym, *["Select Symmetric cipher", "ECB", "CBC", "GCM"])
    drop_asym = tk.OptionMenu(root, clicked_asym, *["Select Asymmetric cipher", "RSA", "RSA-OAEP"])

    # import images for button
    volume_on = tk.PhotoImage(file='Utilities/volume_on.png').subsample(12, 12)
    volume_off = tk.PhotoImage(file='Utilities/volume_off.png').subsample(12, 12)

    # define widget for console outputs
    text_widget0 = tk.Text(root, height=6, width=30, foreground="red")
    text_widget0.insert("1.0", "Welcome to Crypto 8-bit!")
    text_widget0.config(state=tk.DISABLED)

    # adds a frame containing both password widget and button to confirm it
    frame_password = tk.Frame(root)
    frame_popUp = tk.Frame(root)
    frame_search_type = tk.Frame(root)

    # define widget for password input from user as key
    text_widget1 = tk.Entry(frame_password, width=20, foreground="black", show="*")
    text_widget1.config(state=tk.NORMAL)

    # define label for program title
    label0 = tk.Label(root, text="Crypto 8-bit", font=("Helvetica", 24, "bold"), foreground="blue", relief=tk.SUNKEN)

    # define buttons and their configuration
    button_file = tk.Button(frame_search_type, text="Source File", command=open_file)
    button_key = tk.Button(root, text="Source Key", command=source_key)
    button_exit = tk.Button(root, text="Exit", command=on_closing)
    button_start = tk.Button(root, text="Start", command=start)
    button_public = tk.Button(root, text="Source Public Key", command=source_public_key)
    button_private = tk.Button(root, text="Source Private Key", command=source_private_key)
    button_keygen = tk.Button(root, text="Keygen", command=keygen_exe)
    button_password = tk.Button(frame_password, text="Confirm", command=widget_password)
    button_popUp_info = tk.Button(root, text="(i)", command=popup_description)

    # define button for volume toggle off/on
    button_volume = tk.Button(root, image=volume_on, command=volume_toggler)
    button_volume.configure(borderwidth=2, highlightthickness=2)

    # define checkboxes and their configuration
    checkbox_symmetric = tk.Checkbutton(root, text="Checked sym. / Unchecked asym.", variable=is_sym,
                                        command=hide_option)
    checkbox_encryption = tk.Checkbutton(root, text="Checked encrypt. / Unchecked decrypt.", variable=is_encrypt,
                                         command=hide_option)
    checkbox_file_directory = tk.Checkbutton(frame_search_type, variable=is_not_directory, command=update_button_source)

    button_popUp_info.pack(padx=10)
    button_volume.pack(padx=10)
    button_popUp_info.place(x=280, y=10)
    button_volume.place(x=277, y=40)
    label0.pack(side="top", pady=30)
    checkbox_symmetric.pack(pady=0)
    checkbox_encryption.pack(pady=0)
    button_keygen.pack(pady=10)
    drop_asym.pack(pady=10)
    frame_search_type.pack()
    button_file.pack(padx=10, pady=5, side=tk.LEFT)
    checkbox_file_directory.pack(pady=5, side=tk.RIGHT)
    button_key.pack(pady=5)
    button_private.pack(pady=5)
    button_start.pack(pady=10)
    button_exit.pack()
    text_widget0.pack(pady=20)

    # bind the exit event handler to the window's close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # bind with start button
    root.protocol("START", start)

    # load and play the MP3 file
    pygame.mixer.music.load("Utilities/jeremy_blake-powerup.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    root.mainloop()
