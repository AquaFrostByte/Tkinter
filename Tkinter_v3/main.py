import vlc
import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Simple VLC Player")

# Create a label and entry for file path input
label = tk.Label(window, text="File Path")
label.pack()

path_song = tk.Entry(window, width=50)
path_song.pack()

# Initialize VLC MediaPlayer instance
p = vlc.MediaPlayer()

x = True

# Define the main function
def player_main():
    if p.is_playing():
        p.pause()
        player_main_button.config(text="▶ Play")  # Change text to "Resume" when paused
    else:
        file_path = path_song.get()
        p.set_mrl(file_path)
        p.play()
        player_main_button.config(text="⏸ Pause")  # Change text to "Pause" when resumed

    path_now_playing = path_song.get()
    now_playing = path_now_playing.split("/")[-1]
    player_now_playing.config(text=f"now playing:{now_playing}")

def player_stop():
    p.stop()
    player_main_button.config(text="▶ Play")  # Reset and disable Pause button when stopped

player_now_playing = tk.Label(window, text="Waiting for Song")
player_now_playing.pack()

# Create and pack the Pause button (initially disabled)
player_main_button = tk.Button(window, text="▶ Play", width=10, height=2, command=player_main)
player_main_button.pack(side=tk.LEFT, padx=5)

# Create and pack the Stop button (initially disabled)
player_stop_button = tk.Button(window, text="■ Stop", width=10, height=2, command=player_stop)
player_stop_button.pack(side=tk.RIGHT, padx=5)

# Run the Tkinter event loop
window.mainloop()
