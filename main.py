# # In main.py
# from engine import Song, Playlist

# # 1. Create a new playlist
# my_playlist = Playlist()

# # 2. Create some song objects
# song1 = Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355)
# song2 = Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482)
# song3 = Song(song_id="S003", title="Hotel California", artist="Eagles", duration=390)

# # 3. Add songs to the playlist
# my_playlist.add_song(song1)
# my_playlist.add_song(song2)
# my_playlist.add_song(song3)

# # 4. Display the playlist to see the result
# print("My awesome playlist:")
# my_playlist.display()

# # 5. Check the count
# print(f"\n{my_playlist}") # This will use the __repr__ method

# # In main.py, after the previous code

# print("\n--- Testing Deletion ---")
# # Let's delete the middle song, "Stairway to Heaven" (at index 1)
# my_playlist.delete_song(1)
# my_playlist.display()

# print(f"\n{my_playlist}") 

# # Now let's delete the head, "Bohemian Rhapsody" (now at index 0)
# my_playlist.delete_song(0)
# my_playlist.display()

# """Testing the move_song function"""

# # In main.py

# print("\n--- Testing Move ---")
# # Re-create the playlist for a clean test
# move_playlist = Playlist()
# move_playlist.add_song(Song(song_id="S001", title="Song A", artist="Art", duration=100))
# move_playlist.add_song(Song(song_id="S002", title="Song B", artist="Art", duration=100))
# move_playlist.add_song(Song(song_id="S003", title="Song C", artist="Art", duration=100))
# move_playlist.add_song(Song(song_id="S004", title="Song D", artist="Art", duration=100))

# print("Original Playlist:")
# move_playlist.display()

# # Move Song D (index 3) to the beginning (index 0)
# print("\nMoving Song D (index 3) to index 0...")
# move_playlist.move_song(3, 0)
# move_playlist.display()

# # Move Song A (now at index 1) to the end (index 3)
# print("\nMoving Song A (index 1) to index 3...")
# move_playlist.move_song(1, 3)
# move_playlist.display()


# # In main.py
# print("\n--- Testing Reverse ---")
# # Use the same playlist from the 'move' test
# print("Playlist before reverse:")
# move_playlist.display()

# print("\nReversing the playlist...")
# move_playlist.reverse_playlist()

# print("\nPlaylist after reverse:")
# move_playlist.display()

# # In main.py
# from engine import Song, PlayWiseEngine

# # --- Setup ---
# engine = PlayWiseEngine()

# songA = Song(song_id="S001", title="Song A", artist="Art", duration=100)
# songB = Song(song_id="S002", title="Song B", artist="Art", duration=100)
# songC = Song(song_id="S003", title="Song C", artist="Art", duration=100)
# songD = Song(song_id="S004", title="Song D", artist="Art", duration=100)

# engine.playlist.add_song(songA)
# engine.playlist.add_song(songB)
# engine.playlist.add_song(songC)
# engine.playlist.add_song(songD)

# print("--- Testing Playback History ---")
# print("Initial Playlist:")
# engine.playlist.display()

# # --- Simulate Playing Songs ---
# print("\nPlaying two songs...")
# engine.play_song(songA)
# engine.play_song(songB)

# print("\nPlayback History (top of stack is last):", engine.playback_history)

# # --- Undo the Last Played Song ---
# print("\nUndoing the last play...")
# engine.undo_last_play()

# print("\nNew Playback History:", engine.playback_history)
# print("Playlist after undo:")
# engine.playlist.display()


# # In main.py
# print("\n--- Testing Rating Tree ---")
# # Rate the songs we created earlier
# engine.rate_song(songC, 5) # 5 stars
# engine.rate_song(songA, 4) # 4 stars
# engine.rate_song(songB, 5) # Another 5-star song
# engine.rate_song(songD, 2) # 2 stars

# # Display the contents of the tree
# engine.rating_tree.display()

# # In main.py
# print("\n--- Testing Rating Search ---")

# # Search for a rating that exists
# print("Searching for 5-star songs...")
# five_star_songs = engine.rating_tree.search_by_rating(5)
# print(f"Found: {five_star_songs}")

# # Search for a rating that does not exist
# print("\nSearching for 3-star songs...")
# three_star_songs = engine.rating_tree.search_by_rating(3)
# print(f"Found: {three_star_songs}")

# # In main.py
# print("\n--- Testing Rating Deletion ---")

# print("Tree before deletion:")
# engine.rating_tree.display()

# # Delete songB (ID S002), which has a 5-star rating
# print("\nDeleting Song B (ID: S002, Rating: 5)...")
# engine.delete_rated_song("S002", 5)

# print("\nTree after deletion:")
# engine.rating_tree.display()


# #TESTING THE NEW HASH MAP Constant lookup alongwith the insert and delete operations for Synchronization between 2 Different Data Structures , A HashMap and A Doubly Linked List
# # In main.py, you can create a new test section
# from engine import Song, PlayWiseEngine

# # --- Setup ---
# engine = PlayWiseEngine()

# songA = Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355)
# songB = Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482)

# # Use the new synchronized method to add songs
# engine.add_song_to_playlist(songA)
# engine.add_song_to_playlist(songB)

# print("\n--- Testing Instant Lookup ---")
# print("Playlist contents:")
# engine.playlist.display()

# print("\nLooking up song S002...")
# found_song = engine.lookup_song("S002")
# print(f"Found: {found_song}")
# print(f"Its duration is: {found_song.duration}s")


# print("\nDeleting song at index 0...")
# engine.delete_song_from_playlist(0)

# print("\nLooking up song S001 (should be gone)...")
# found_song = engine.lookup_song("S001")
# print(f"Found: {found_song}")

# # In main.py
# print("\n--- Testing Sorting ---")

# # Create an unsorted playlist
# sort_engine = PlayWiseEngine()
# sort_engine.add_song_to_playlist(Song(song_id="S003", title="Hotel California", artist="Eagles", duration=390))
# sort_engine.add_song_to_playlist(Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355))
# sort_engine.add_song_to_playlist(Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482))

# print("Original playlist:")
# sort_engine.playlist.display()

# # Sort by title (alphabetical)
# print("\nSorting by title...")
# sort_engine.playlist.sort_playlist(by_key='title')
# sort_engine.playlist.display()

# # Sort by duration (longest first)
# print("\nSorting by duration (descending)...")
# sort_engine.playlist.sort_playlist(by_key='duration', reverse=True)
# sort_engine.playlist.display()

# # In main.py
# import json

# print("\n--- Testing System Snapshot ---")

# # Let's use the 'sort_engine' which already has songs and ratings
# # Let's add some playback history to it
# for song in sort_engine.playlist.head, sort_engine.playlist.head.next:
#     sort_engine.play_song(song.song)

# # Generate and print the snapshot
# final_snapshot = sort_engine.export_snapshot()

# # Use json.dumps for pretty printing the dictionary
# print(json.dumps(final_snapshot, default=lambda o: o.__dict__, indent=4))

# # In main.py
# print("\n--- Testing Volume Normalization ---")
# norm_playlist = Playlist()
# norm_playlist.add_song(Song("V01", "Loud Song", "Artist", 180, volume=100))
# norm_playlist.add_song(Song("V02", "Quiet Song", "Artist", 180, volume=50))
# norm_playlist.add_song(Song("V03", "Medium Song", "Artist", 180, volume=75))

# norm_playlist.normalize_volume()

# # In main.py
# from engine import Song, PlayWiseEngine

# # --- Setup ---
# engine = PlayWiseEngine()
# engine.create_playlist("my_favorites") # Creates a new playlist and sets it as active

# # Get the active playlist object from the dictionary
# active_playlist = engine.playlists[engine.active_playlist_id]

# # Now add songs to that specific playlist
# songA = Song(song_id="S001", title="Bohemian Rhapsody", artist="Queen", duration=355)
# songB = Song(song_id="S002", title="Stairway to Heaven", artist="Led Zeppelin", duration=482)

# active_playlist.add_song(songA)
# active_playlist.add_song(songB)

# # Now you can test other features
# print("Playlist contents:")
# active_playlist.display()

# In main.py

"""The Older test cases were accessing a method where the specialized use cases weren't Implemented, hence a concise set of test cases for all the relevant methods has been written down below as follows """

import json
from engine import Song, PlayWiseEngine

# ====================================================================
# SETUP
# ====================================================================
print("INITIALIZING ENGINE...")
engine = PlayWiseEngine()

# Create song objects to be used in tests
song1 = Song("S001", "Bohemian Rhapsody", "Queen", 355, 85)
song2 = Song("S002", "Stairway to Heaven", "Led Zeppelin", 482, 75)
song3 = Song("S003", "Hotel California", "Eagles", 390, 90)
song4 = Song("S004", "Imagine", "John Lennon", 183, 60)

# ====================================================================
# 1. CORE PLAYLIST & HASHMAP (LOOKUP) TESTS
# ====================================================================
print("\n--- 1. Testing Core Playlist & HashMap Sync ---")
engine.create_playlist("rock_classics")

# Test adding songs (tests both linked list and hashmap sync)
engine.add_song_to_playlist("rock_classics", song1)
engine.add_song_to_playlist("rock_classics", song2)
engine.add_song_to_playlist("rock_classics", song3)

# Display playlist contents
print("\nInitial Playlist 'rock_classics':")
engine.playlists["rock_classics"].display()

# Test HashMap instant lookup
print("\nTesting instant lookup for song S002...")
looked_up_song = engine.lookup_song("S002")
print(f"Found: {looked_up_song}")

# Test deletion (tests both linked list and hashmap sync)
print("\nTesting deletion of song at index 1...")
engine.delete_song_from_playlist("rock_classics", 1) # Deleting "Stairway to Heaven"
engine.playlists["rock_classics"].display()
print(f"Trying to look up deleted song S002 again: {engine.lookup_song('S002')}")

# ====================================================================
# 2. ADVANCED PLAYLIST OPERATION TESTS
# ====================================================================
print("\n--- 2. Testing Advanced Playlist Operations ---")
# Re-add a song for the tests
engine.add_song_to_playlist("rock_classics", song4)
print("\nPlaylist before operations:")
engine.playlists["rock_classics"].display()

# Test move_song
print("\nMoving song at index 2 ('Imagine') to index 0...")
engine.playlists["rock_classics"].move_song(2, 0)
engine.playlists["rock_classics"].display()

# Test reverse_playlist
print("\nReversing playlist...")
engine.playlists["rock_classics"].reverse_playlist()
engine.playlists["rock_classics"].display()

# Test sort_playlist
print("\nSorting playlist by duration (ascending)...")
engine.playlists["rock_classics"].sort_playlist(by_key='duration')
engine.playlists["rock_classics"].display()


# ====================================================================
# 3. RATING TREE (BST) TESTS
# ====================================================================
print("\n--- 3. Testing Rating Tree (BST) ---")
engine.rate_song(song1, 5) # Rate "Bohemian Rhapsody"
engine.rate_song(song3, 5) # Rate "Hotel California"
engine.rate_song(song4, 4) # Rate "Imagine"

print("\nDisplaying tree contents (in-order traversal):")
engine.rating_tree.display()

print("\nSearching for 5-star songs...")
print(f"Found: {engine.rating_tree.search_by_rating(5)}")


# ====================================================================
# 4. HISTORY STACK & MULTI-PLAYLIST TESTS
# ====================================================================
print("\n--- 4. Testing History Stack & Multi-Playlist Features ---")
# "Play" some songs from the active playlist
engine.play_song(song1)
engine.play_song(song4)
print(f"Playback History: {engine.playback_history}")

# Test undo
print("\nUndoing last play...")
engine.undo_last_play() # Re-adds "Imagine" to the active playlist
print(f"New Playback History: {engine.playback_history}")
print("Active playlist after undo:")
engine.playlists["rock_classics"].display()

# Test Pause/Resume
print("\nCreating and switching to a new 'road_trip' playlist...")
engine.create_playlist("road_trip")
engine.switch_playlist("road_trip", current_song_index=3) # "Pauses" rock_classics
print(f"Pause Stack: {engine.pause_stack}")

print("\nResuming last playlist...")
engine.resume_last_playlist()
print(f"Current active playlist is now: '{engine.active_playlist_id}'")


# ====================================================================
# 5. FINAL SYSTEM SNAPSHOT
# ====================================================================
print("\n--- 5. Generating Final System Snapshot ---")
final_snapshot = engine.export_snapshot()
# Use json.dumps for pretty printing the final state
print(json.dumps(final_snapshot, default=lambda o: o.__dict__, indent=4))