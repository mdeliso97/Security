import tkinter as tk
import pygame

from ECB import *
from CBC import *
from AES_GCM import *


def on_button0_click():
    label0.config(text="Button Clicked!")


def on_button1_click():
    label0.config(text="Button Clicked!")


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


def menu0_action0():
    ecb(label0)


def menu0_action1():
    cbc(label0)


def menu0_action2():
    aes_gcm(label0)


# Change the label text
def show0():
    label0.config(text=clicked0.get())


def show1():
    label0.config(text=clicked1.get())


if __name__ == '__main__':
    # Initialize pygame
    pygame.mixer.init()

    root = tk.Tk()
    root.title("Cypher 8-bit")

    # Define a custom font and foreground color for the title
    title_font = ("Helvetica", 24, "bold")  # Change the font family, size, and style
    title_color = "blue"  # Change the text color

    # Adjust size
    root.geometry("300x400")

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

    button0 = tk.Button(root, text="menu", command=show0)
    button1 = tk.Button(root, text="menu", command=show1)
    button2 = tk.Button(root, text="Source File", command=on_button0_click)
    button3 = tk.Button(root, text="Source Key", command=on_button1_click)
    button4 = tk.Button(root, text="Exit", command=on_closing)

    label0.pack(pady=20)
    drop0.pack(pady=10)
    drop1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=20)
    button4.pack(pady=10)

    # Bind the exit event handler to the window's close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Load and play the MP3 file
    pygame.mixer.music.load("jeremy_blake-powerup.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    root.mainloop()
