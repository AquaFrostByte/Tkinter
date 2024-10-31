import vlc
import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Simple VLC Player")

# Create a label and entry for file path input
label = tk.Label(window, text="File Path")
label.grid(row=0, column=0, padx=1, pady=5)

path_song = tk.Entry(window, width=50)
path_song.grid(row=0, column=1, padx=1, pady=5)

# Initialize VLC MediaPlayer instance
p = vlc.MediaPlayer()

# Define the play function
def player_play():
    file_path = path_song.get()
    p.set_mrl(file_path)
    p.play()
    player_pause_button.config(text="⏸ Pause")  # Enable Pause button when playing
    player_stop_button.config(state=tk.NORMAL)  # Enable Stop button when playing

    path_now_playing = path_song.get()
    now_playing = path_now_playing.split("/")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")

# Define the stop function
def player_stop():
    p.stop()
    player_pause_button.config(text="⏸ Pause")  # Reset and disable Pause button when stopped
    player_stop_button.config(state=tk.DISABLED)  # Disable Stop button when stopped

# Define the pause function
def player_pause():
    if p.is_playing():
        p.pause()
        player_pause_button.config(text="▶ Resume")  # Change text to "Resume" when paused
    else:
        p.play()
        player_pause_button.config(text="⏸ Pause")  # Change text to "Pause" when resumed

# Display the label showing the current status
player_now_playing = tk.Label(window, text="waiting for song...")
player_now_playing.grid(row=1, column=0, columnspan=2, pady=5)

# Create and grid the Play button
player_play_button = tk.Button(window, text="▶ Play", width=10, height=2, command=player_play)
player_play_button.grid(row=2, column=0, padx=1, pady=5)

# Create and grid the Pause button
player_pause_button = tk.Button(window, text="⏸ Pause", width=10, height=2, command=player_pause)
player_pause_button.grid(row=2, column=1, padx=1, pady=5)

# Create and grid the Stop button (initially disabled)
player_stop_button = tk.Button(window, text="■ Stop", width=10, height=2, command=player_stop, state=tk.DISABLED)
player_stop_button.grid(row=2, column=2, padx=1, pady=5)

# Run the Tkinter event loop
window.mainloop()
