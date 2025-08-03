# In main.py
from engine import Song, Playlist

# 1. Create a new playlist
my_playlist = Playlist()

# 2. Create some song objects
song1 = Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355)
song2 = Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482)
song3 = Song(song_id="S003", title="Hotel California", artist="Eagles", duration=390)

# 3. Add songs to the playlist
my_playlist.add_song(song1)
my_playlist.add_song(song2)
my_playlist.add_song(song3)

# 4. Display the playlist to see the result
print("My awesome playlist:")
my_playlist.display()

# 5. Check the count
print(f"\n{my_playlist}") # This will use the __repr__ method

# In main.py, after the previous code

print("\n--- Testing Deletion ---")
# Let's delete the middle song, "Stairway to Heaven" (at index 1)
my_playlist.delete_song(1)
my_playlist.display()

print(f"\n{my_playlist}") 

# Now let's delete the head, "Bohemian Rhapsody" (now at index 0)
my_playlist.delete_song(0)
my_playlist.display()

"""Testing the move_song function"""

# In main.py

print("\n--- Testing Move ---")
# Re-create the playlist for a clean test
move_playlist = Playlist()
move_playlist.add_song(Song(song_id="S001", title="Song A", artist="Art", duration=100))
move_playlist.add_song(Song(song_id="S002", title="Song B", artist="Art", duration=100))
move_playlist.add_song(Song(song_id="S003", title="Song C", artist="Art", duration=100))
move_playlist.add_song(Song(song_id="S004", title="Song D", artist="Art", duration=100))

print("Original Playlist:")
move_playlist.display()

# Move Song D (index 3) to the beginning (index 0)
print("\nMoving Song D (index 3) to index 0...")
move_playlist.move_song(3, 0)
move_playlist.display()

# Move Song A (now at index 1) to the end (index 3)
print("\nMoving Song A (index 1) to index 3...")
move_playlist.move_song(1, 3)
move_playlist.display()


# In main.py
print("\n--- Testing Reverse ---")
# Use the same playlist from the 'move' test
print("Playlist before reverse:")
move_playlist.display()

print("\nReversing the playlist...")
move_playlist.reverse_playlist()

print("\nPlaylist after reverse:")
move_playlist.display()