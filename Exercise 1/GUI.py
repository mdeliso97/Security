import tkinter as tk
import pygame

import encryption
from encryption import *


def on_button0_click():
    label.config(text="Button Clicked!")


def on_button1_click():
    label.config(text="Button Clicked!")


# Define an exit event handler to stop the audio
def on_closing():
    pygame.mixer.music.stop()  # Stop the audio playback
    root.destroy()


def menu_action0():
    encryption.ecb(label)


def menu_action1():
    encryption.cbc(label)


# Change the label text
def show():
    label.config(text=clicked.get())


if __name__ == '__main__':

    # Initialize pygame
    pygame.mixer.init()

    root = tk.Tk()
    root.title("Cypher 8-bit")

    # Define a custom font and foreground color for the title
    title_font = ("Helvetica", 24, "bold")  # Change the font family, size, and style
    title_color = "blue"  # Change the text color

    # Adjust size
    root.geometry("300x240")

    # Dropdown menu options
    options = [
        "ECB",
        "CBC"
    ]

    # datatype of menu text
    clicked = tk.StringVar()

    # initial menu text
    clicked.set("Select Method")

    # Create Dropdown menu
    drop = tk.OptionMenu(root, clicked, *options)

    # menu0 = tk.Menu(root, title="Select Method")
    # root.config(menu=menu0)

    # menu0.add_cascade(label="File", menu=menu0)
    # menu0.add_command(label="ECB", command=menu_action0)
    # menu0.add_command(label="CBC", command=menu_action1)
    # menu0.add_command(label="Menu Item 2", command=menu_action2)

    label = tk.Label(root, text="Cypher 8-bit", font=title_font, foreground=title_color)

    button0 = tk.Button(root, text="menu", command=show)
    button1 = tk.Button(root, text="Source File", command=on_button0_click)
    button2 = tk.Button(root, text="Source Key", command=on_button1_click)
    button3 = tk.Button(root, text="Exit", command=on_closing)

    label.pack(pady=20)
    drop.pack()
    button1.pack(pady=10)
    button2.pack(pady=10)
    button3.pack()

    # Bind the exit event handler to the window's close button
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Load and play the MP3 file
    pygame.mixer.music.load("jeremy_blake-powerup.mp3")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    root.mainloop()
