import vlc
import tkinter as tk
import os
import time

status = ""

def player_files(folder_path):
    # Supported media extensions (you can add or remove formats as needed)
    media_extensions = ('.mp3','.wav','.ogg')

    media_files = [
        os.path.join(folder_path, file) for file in os.listdir(folder_path)
        if file.endswith(media_extensions)
    ]
    return media_files
   
def player_play(media_file):

    player = vlc.MediaPlayer(media_file)
    player.play()

    # Wait until the media finishes playing
    while player.is_playing():
        time.sleep(1)
    
    # Stop the player after playback
    player.stop()

def main():
    # Specify your folder path containing media files
    folder_path = entry

    # Get all media files from the folder
    media_files = get_media_files(folder_path)

    if not media_files:
        status = "No media files found in the specified folder."
        tk.update
        return
        
window = tk.Tk()
window.title("Simple VLC Player")

label = tk.Label(window, text="File Path")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="PLAY!", width=25, height=5, command=player_play)
button.pack()

Player_now = tk.Label(window, text=os.path.basename(media_file))
Player_now.pack()

Player_status = tk.Label(window, text=os.path.basename(media_file))
Player_status.pack()


window.mainloop()