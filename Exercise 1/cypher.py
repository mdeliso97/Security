import tkinter as tk
from tkinter import filedialog
import functools
import pygame

from ECB import *
from CBC import *
from AES_GCM import *
from RES import *


def open_file():
    global content

    file_path = filedialog.askopenfilename(
        title="Select a .txt file", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])  # Specify file types

    if file_path:
        if file_path.endswith(".txt"):
            # Read and process the .txt file
            label1.config(text="Success: file stored successfully!")

            with open(file_path, "r") as file:
                content = file.read()
                # print content
                print("File content:\n", content)
        else:
            label1.config(text="Error: selected file is not a .txt file!")


def on_button1_click():
    label1.config(text="Button Clicked!")


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


# def bool_case():
#     if is_encrypt:
#         is_encrypt = False
#
#     else:
#         is_encrypt = True


def start():
    print(clicked0.get())
    print(clicked1.get())
    if clicked0.get() == "ECB" and clicked1.get() == "RES":
        message = ecb(content, is_encrypt)

        # Write the result to a new text file
        with open("output.txt", "w") as output_file:
            output_file.write(message)
            label1.config(text="Success: result written to output.txt")

    elif clicked0.get() == "CBC" and clicked1.get() == "RES":
        message = cbc(content, is_encrypt)

        # Write the result to a new text file
        with open("output.txt", "w") as output_file:
            output_file.write(message)
            label1.config(text="Success: result written to output.txt")


if __name__ == '__main__':
    # Initialize pygame
    pygame.mixer.init()

    global content
    global is_encrypt

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
    button2 = tk.Button(root, text="Source File", command=open_file)
    button3 = tk.Button(root, text="Source Key", command=on_button1_click)
    button4 = tk.Button(root, text="Exit", command=on_closing)
    button5 = tk.Button(root, text="Start", command=start)

    is_encrypt = tk.BooleanVar()
    checkbox0 = tk.Checkbutton(root, text="Checked encrypt. / Unchecked decrypt.", variable=is_encrypt)

    label0.pack(pady=20)
    drop0.pack(pady=10)
    drop1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=20)
    checkbox0.pack(pady=10)
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
