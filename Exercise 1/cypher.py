import tkinter as tk
from tkinter import filedialog

import pygame

from ECB import *
from CBC import *
from AES_GCM import *
from RES import *


def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select a .txt file", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])  # Specify file types

    if file_path:
        if file_path.endswith(".txt"):
            # Read and process the .txt file
            label1.config(text="Success: file stored successfully!")

            with open(file_path, "r") as file:
                content = file.read()
                # Do something with the content
                print("File content:\n", content)
        else:
            label1.config(text="Error: selected file is not a .txt file!")
            file_path = "Empty"
    return file_path


def on_button1_click():
    label1.config(text="Button Clicked!")


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


def start():
    print(clicked0.get())
    print(clicked1.get())
    if clicked0.get() == "ECB" and clicked1.get() == "RES":
        print("ecb")
        #ecb(file)
        #res(file)

    elif clicked0.get() == "CBC" and clicked1.get() == "RES":
        print("cbc")
        #cbc(file)
        #res(file)


def menu0_action0():
    ecb(label0)


def menu0_action1():
    cbc(label0)


def menu0_action2():
    aes_gcm(label0)


# Change the label text
# def show0():
#     label0.config(text=clicked0.get())
#     user_input0 = clicked0.get()
#     print(user_input0)
#     return user_input0
#
#
# def show1():
#     label0.config(text=clicked1.get())
#     user_input1 = clicked1.get()
#     print(user_input1)
#     return user_input1


if __name__ == '__main__':
    # Initialize pygame
    pygame.mixer.init()

    root = tk.Tk()
    root.title("Cypher 8-bit")

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

    label0 = tk.Label(root, text="Cypher 8-bit", font=title_font, foreground=title_color)
    label1 = tk.Label(root, text="Welcome!", font=11, foreground="red")

    # button0 = tk.Button(root, text="menu", command=show0)
    # button1 = tk.Button(root, text="menu", command=show1)
    button2 = tk.Button(root, text="Source File", command=open_file_dialog)
    button3 = tk.Button(root, text="Source Key", command=on_button1_click)
    button4 = tk.Button(root, text="Exit", command=on_closing)
    button5 = tk.Button(root, text="Start", command=start)

    label0.pack(pady=20)
    drop0.pack(pady=10)
    drop1.pack(pady=10)
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
