import vlc
import tkinter as tk
import os
import time
from tkinter import messagebox

# Global status variable to keep track of current status
status = ""

def get_media_files(folder_path):
    """
    Get all media files from the given folder.
    """
    # Supported media extensions (you can add or remove formats as needed)
    media_extensions = ('.mp3', '.wav', '.ogg')

    # Get a list of files in the folder with supported extensions
    media_files = [
        os.path.join(folder_path, file) for file in os.listdir(folder_path)
        if file.endswith(media_extensions)
    ]
    
    return media_files

def play_media_file(media_file):
    """
    Play a single media file.
    """
    if not media_file:
        messagebox.showwarning("Warning", "No media file selected!")
        return

    player = vlc.MediaPlayer(media_file)
    player.play()
    
    # Update status
    Player_now.config(text=f"Now Playing: {os.path.basename(media_file)}")
    
    # Wait until the media finishes playing
    while player.is_playing():
        window.update()
        time.sleep(0.5)
    
    # Stop the player after playback
    player.stop()
    Player_now.config(text="Playback finished.")

def on_play_button_click():
    """
    Get the selected file and play it.
    """
    folder_path = entry.get()
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    # Get all media files in the folder
    media_files = get_media_files(folder_path)
    
    if not media_files:
        Player_status.config(text="No media files found in the specified folder.")
        return

    # If a file is selected from the listbox, get the selected file path
    try:
        selected_index = media_listbox.curselection()[0]
        selected_media_file = media_files[selected_index]
        print(selected_media_file)
        play_media_file(selected_media_file)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a file from the list!")

def update_media_list():
    """
    Update the media file list based on the folder path.
    """
    folder_path = entry.get()
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    media_files = get_media_files(folder_path)
    
    # Clear the current list
    media_listbox.delete(0, tk.END)

    if not media_files:
        Player_status.config(text="No media files found in the specified folder.")
    else:
        # Insert media files into the listbox
        for file in media_files:
            media_listbox.insert(tk.END, os.path.basename(file))
        Player_status.config(text="Media files loaded. Select a file to play.")

# Create the main window
window = tk.Tk()
window.title("Simple VLC Player")

# Folder path input
label = tk.Label(window, text="Folder Path")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Button to update the media list
load_button = tk.Button(window, text="Load Media Files", command=update_media_list)
load_button.pack()

# Listbox to display media files
media_listbox = tk.Listbox(window, width=50, height=10)
media_listbox.pack()

# Play button
play_button = tk.Button(window, text="PLAY!", width=25, height=2, command=on_play_button_click)
play_button.pack()

# Labels to show playback status
Player_now = tk.Label(window, text="Now Playing: None")
Player_now.pack()

Player_status = tk.Label(window, text="Status: No media files loaded.")
Player_status.pack()

# Run the application
window.mainloop()
