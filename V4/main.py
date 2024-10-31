import vlc
import tkinter as tk
import os

# Initialize the main window
window = tk.Tk()
window.title("Simple VLC Player")

frame1 = tk.Frame(window, relief="solid")
frame1.grid(row=0, column=0, pady=1)

frame2 = tk.Frame(window, relief="solid")
frame2.grid(row=1, column=0, pady=1)  # Place the frame using grid

# Create a label and entry for file path input
label = tk.Label(frame1, text="File Path:")
label.grid(row=0, column=0, padx=1, pady=5)

path_song = tk.Entry(frame1, width=80,)
path_song.grid(row=0, column=1, padx=1, pady=5)

# Initialize VLC MediaPlayer instance
p = vlc.MediaPlayer()
song = 0
song_count = -1

media_list = []

def load_songs():
    global song_count
    global song

    song = 0
    song_count = -1

    file_path = path_song.get()
    print("cheack")
    # Recursively list all files in the file_path
    if not os.path.exists(file_path):
        print(f"Directory '{file_path}' does not exist.")
    else:
        # Walk through the file_path
        for root, dirs, files in os.walk(file_path):
            print("check2")  # Corrected print statement
            for file in files:
                print(os.path.join(root, file))
                media_list.append(os.path.join(root, file))
                song_count = song_count + 1


def skip_song():
    global song
    song = song + 1
    print(song)
    if song > song_count:
        print("no next")
        song = 0
    p.set_mrl(media_list[song])
    p.play()
    now_playing = media_list[song].split("/")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")

def previous_song():
    global song
    song = song - 1
    print(song)
    if song == -1:
        print("out of range")
        song = song_count
    p.set_mrl(media_list[song])
    p.play()
    now_playing = media_list[song].split("/")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")

# Define the play function
def player_play():
    file_path = path_song.get()
    song = 0
    p.set_mrl(media_list[song])
    p.play()
    player_pause_button.config(text="⏸ Pause")  # Enable Pause button when playing
    player_stop_button.config(state=tk.NORMAL)  # Enable Stop button when playing

    now_playing = media_list[song].split("/")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")

# Define the stop function
def player_stop():
    p.stop()

    global song_count
    global song

    song = 0
    song_count = -1

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
player_now_playing = tk.Label(frame1, text="waiting for song...")
player_now_playing.grid(row=1, column=0, columnspan=2, pady=5)

# Create and grid the Play button
player_play_button = tk.Button(frame2, text="▶ Play", width=10, height=2, command=player_play)
player_play_button.grid(row=2, column=0, padx=1, pady=5)

player_skip_button = tk.Button(frame2, text="⏭ Skip", width=10, height=2, command=skip_song)
player_skip_button.grid(row=2, column=3, padx=1, pady=5)

player_skip_button = tk.Button(frame2, text="⏮ Previous", width=10, height=2, command=previous_song)
player_skip_button.grid(row=2, column=1, padx=1, pady=5)
# Create and grid the Pause button
player_pause_button = tk.Button(frame2, text="⏸ Pause", width=10, height=2, command=player_pause)
player_pause_button.grid(row=2, column=2, padx=1, pady=5)

# Create and grid the Stop button (initially disabled)
player_stop_button = tk.Button(frame2, text="■ Stop", width=10, height=2, command=player_stop, state=tk.DISABLED)
player_stop_button.grid(row=2, column=4, padx=1, pady=5)

player_load_button = tk.Button(frame1, text="Load", width=5, height=1, command=load_songs)
player_load_button.grid(row=0, column=2, padx=1, pady=5)

# Run the Tkinter event loop
window.mainloop()
