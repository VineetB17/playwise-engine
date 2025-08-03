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

# In main.py
from engine import Song, PlayWiseEngine

# --- Setup ---
engine = PlayWiseEngine()

songA = Song(song_id="S001", title="Song A", artist="Art", duration=100)
songB = Song(song_id="S002", title="Song B", artist="Art", duration=100)
songC = Song(song_id="S003", title="Song C", artist="Art", duration=100)
songD = Song(song_id="S004", title="Song D", artist="Art", duration=100)

engine.playlist.add_song(songA)
engine.playlist.add_song(songB)
engine.playlist.add_song(songC)
engine.playlist.add_song(songD)

print("--- Testing Playback History ---")
print("Initial Playlist:")
engine.playlist.display()

# --- Simulate Playing Songs ---
print("\nPlaying two songs...")
engine.play_song(songA)
engine.play_song(songB)

print("\nPlayback History (top of stack is last):", engine.playback_history)

# --- Undo the Last Played Song ---
print("\nUndoing the last play...")
engine.undo_last_play()

print("\nNew Playback History:", engine.playback_history)
print("Playlist after undo:")
engine.playlist.display()


# In main.py
print("\n--- Testing Rating Tree ---")
# Rate the songs we created earlier
engine.rate_song(songC, 5) # 5 stars
engine.rate_song(songA, 4) # 4 stars
engine.rate_song(songB, 5) # Another 5-star song
engine.rate_song(songD, 2) # 2 stars

# Display the contents of the tree
engine.rating_tree.display()

# In main.py
print("\n--- Testing Rating Search ---")

# Search for a rating that exists
print("Searching for 5-star songs...")
five_star_songs = engine.rating_tree.search_by_rating(5)
print(f"Found: {five_star_songs}")

# Search for a rating that does not exist
print("\nSearching for 3-star songs...")
three_star_songs = engine.rating_tree.search_by_rating(3)
print(f"Found: {three_star_songs}")

# In main.py
print("\n--- Testing Rating Deletion ---")

print("Tree before deletion:")
engine.rating_tree.display()

# Delete songB (ID S002), which has a 5-star rating
print("\nDeleting Song B (ID: S002, Rating: 5)...")
engine.delete_rated_song("S002", 5)

print("\nTree after deletion:")
engine.rating_tree.display()


#TESTING THE NEW HASH MAP Constant lookup alongwith the insert and delete operations for Synchronization between 2 Different Data Structures , A HashMap and A Doubly Linked List
# In main.py, you can create a new test section
from engine import Song, PlayWiseEngine

# --- Setup ---
engine = PlayWiseEngine()

songA = Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355)
songB = Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482)

# Use the new synchronized method to add songs
engine.add_song_to_playlist(songA)
engine.add_song_to_playlist(songB)

print("\n--- Testing Instant Lookup ---")
print("Playlist contents:")
engine.playlist.display()

print("\nLooking up song S002...")
found_song = engine.lookup_song("S002")
print(f"Found: {found_song}")
print(f"Its duration is: {found_song.duration}s")


print("\nDeleting song at index 0...")
engine.delete_song_from_playlist(0)

print("\nLooking up song S001 (should be gone)...")
found_song = engine.lookup_song("S001")
print(f"Found: {found_song}")

# In main.py
print("\n--- Testing Sorting ---")

# Create an unsorted playlist
sort_engine = PlayWiseEngine()
sort_engine.add_song_to_playlist(Song(song_id="S003", title="Hotel California", artist="Eagles", duration=390))
sort_engine.add_song_to_playlist(Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355))
sort_engine.add_song_to_playlist(Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482))

print("Original playlist:")
sort_engine.playlist.display()

# Sort by title (alphabetical)
print("\nSorting by title...")
sort_engine.playlist.sort_playlist(by_key='title')
sort_engine.playlist.display()

# Sort by duration (longest first)
print("\nSorting by duration (descending)...")
sort_engine.playlist.sort_playlist(by_key='duration', reverse=True)
sort_engine.playlist.display()

# In main.py
import json

print("\n--- Testing System Snapshot ---")

# Let's use the 'sort_engine' which already has songs and ratings
# Let's add some playback history to it
for song in sort_engine.playlist.head, sort_engine.playlist.head.next:
    sort_engine.play_song(song.song)

# Generate and print the snapshot
final_snapshot = sort_engine.export_snapshot()

# Use json.dumps for pretty printing the dictionary
print(json.dumps(final_snapshot, default=lambda o: o.__dict__, indent=4))
