
class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration # in seconds

    def __repr__(self):
        # A handy representation for printing
        return f"Song({self.title} by {self.artist})"
    
class PlaylistNode:
    """A node in the doubly linked list for the playlist."""
    def __init__(self, song):
        self.song = song      # The data (a Song object)
        self.next = None      # Pointer to the next node in the list
        self.prev = None      # Pointer to the previous node in the list

class Playlist:
    """Manages the collection of songs using a doubly linked list."""
    def __init__(self):
        self.head = None  # The first song in the playlist
        self.tail = None  # The last song in the playlist
        self.count = 0    # Total number of songs

    def __repr__(self):
        return f"Playlist(songs={self.count})"
    
    # This method goes inside the Playlist class
    def add_song(self, song):
        """Adds a new song to the end of the playlist.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        new_node = PlaylistNode(song)
        
        if self.head is None:
            # If the playlist is empty, the new song is both the head and the tail
            self.head = new_node
            self.tail = new_node
        else:
            # If the playlist is not empty, link the new node after the current tail
            self.tail.next = new_node
            new_node.prev = self.tail
            # Update the tail to be the new node
            self.tail = new_node
            
        self.count += 1

    # This method goes inside the Playlist class
    def delete_song(self, index):
        """Deletes a song from the playlist at a specific index.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # 1. Validate the index
        if not (0 <= index < self.count):
            print(f"Error: Index {index} is out of bounds.")
            return

        # 2. Find the node to delete
        # For small lists, simple traversal is fine.
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        
        # 3. Rewire pointers based on the node's position
        if self.count == 1:
            # Case A: Deleting the only song
            self.head = None
            self.tail = None
        elif current_node == self.head:
            # Case B: Deleting the head
            self.head = self.head.next
            self.head.prev = None
        elif current_node == self.tail:
            # Case C: Deleting the tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # Case D: Deleting a middle node
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

        self.count -= 1
        print(f"Deleted '{current_node.song.title}' from the playlist.")

    # Replace the old move_song method with this one
    def move_song(self, from_index, to_index):
        """Moves a song from one position to another in the playlist.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not (0 <= from_index < self.count and 0 <= to_index < self.count):
            print("Error: Invalid index.")
            return
        if from_index == to_index:
            return

        # --- Step 1: Find and Unlink the node ---
        node_to_move = self.head
        for _ in range(from_index):
            node_to_move = node_to_move.next
        
        if self.count == 1: # Should not happen if from_index != to_index, but good practice
            return

        if node_to_move == self.head:
            self.head = node_to_move.next
        if node_to_move == self.tail:
            self.tail = node_to_move.prev
        
        if node_to_move.prev:
            node_to_move.prev.next = node_to_move.next
        if node_to_move.next:
            node_to_move.next.prev = node_to_move.prev
        
        # --- Step 2: Re-insert the node at the new position (CORRECTED LOGIC) ---
        if to_index == 0:
            # Insert at the head
            node_to_move.next = self.head
            self.head.prev = node_to_move
            self.head = node_to_move
            node_to_move.prev = None
        elif to_index >= self.count - 1:
            # Insert at the tail (This is the new case we added)
            node_to_move.prev = self.tail
            self.tail.next = node_to_move
            self.tail = node_to_move
            node_to_move.next = None
        else:
            # Insert in the middle
            target_node = self.head
            for _ in range(to_index):
                target_node = target_node.next
            
            node_to_move.prev = target_node.prev
            node_to_move.next = target_node
            target_node.prev.next = node_to_move
            target_node.prev = node_to_move

    # This method goes inside the Playlist class
    def reverse_playlist(self):
        """Reverses the entire playlist in-place.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.count < 2:
            # No need to reverse if 0 or 1 songs
            return

        current_node = self.head
        while current_node is not None:
            # Swap the prev and next pointers of the current node
            # A temporary variable 'temp' is needed for the swap
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            
            # Move to the next node in the original list
            # which is now the 'prev' pointer after the swap
            current_node = current_node.prev
        
        # Finally, swap the head and tail pointers of the playlist itself
        temp = self.head
        self.head = self.tail
        self.tail = temp
        print("Playlist has been reversed.")
 

    def display(self):
        """Prints the songs in the playlist from head to tail."""
        if self.head is None:
            print("Playlist is empty.")
            return
        
        current_node = self.head
        song_number = 1
        while current_node is not None:
            song = current_node.song
            print(f"{song_number}. {song.title} by {song.artist} ({song.duration}s)")
            current_node = current_node.next
            song_number += 1

    # These methods go inside the Playlist class
    def sort_playlist(self, by_key='title', reverse=False):
        """
        Sorts the playlist using Merge Sort based on a given key.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if self.count < 2:
            return # No need to sort

        # 1. Extract songs to a Python list
        songs_list = []
        current_node = self.head
        while current_node:
            songs_list.append(current_node.song)
            current_node = current_node.next

        # 2. Sort the list using our Merge Sort implementation
        sorted_songs = self._merge_sort(songs_list, by_key, reverse)

        # 3. Clear and rebuild the linked list
        self.head = None
        self.tail = None
        self.count = 0
        for song in sorted_songs:
            self.add_song(song) # Re-use the add_song method
        
        print(f"Playlist sorted by {by_key} ({'desc' if reverse else 'asc'}).")

    def _merge_sort(self, songs, key, reverse):
        """Private recursive Merge Sort algorithm."""
        if len(songs) <= 1:
            return songs

        # Divide the list into two halves
        mid = len(songs) // 2
        left_half = self._merge_sort(songs[:mid], key, reverse)
        right_half = self._merge_sort(songs[mid:], key, reverse)

        # Combine (merge) the sorted halves
        sorted_list = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            # Use getattr to dynamically access the sort key (e.g., song.title)
            left_val = getattr(left_half[i], key)
            right_val = getattr(right_half[j], key)
            
            # Check for ascending or descending order
            if (not reverse and left_val < right_val) or \
               (reverse and left_val > right_val):
                sorted_list.append(left_half[i])
                i += 1
            else:
                sorted_list.append(right_half[j])
                j += 1

        sorted_list.extend(left_half[i:])
        sorted_list.extend(right_half[j:])
        return sorted_list

# In engine.py, after the Playlist class

class PlayWiseEngine:
    """The main engine to manage all components of the music player."""

    def __init__(self):
        self.playlist = Playlist()
        self.playback_history = []
        self.rating_tree = RatingBST()
        self.song_lookup_table = {}  # <-- ADD THIS: Our HashMap

    # NEW METHOD
    def add_song_to_playlist(self, song):
        """Adds a song to the playlist and the lookup table."""
        self.playlist.add_song(song)
        self.song_lookup_table[song.song_id] = song
        print(f"Added '{song.title}' to playlist and lookup table.")

    # NEW METHOD
    def delete_song_from_playlist(self, index):
        """Deletes a song from the playlist and the lookup table."""
        # We need to get the song object before deleting it from the playlist
        node_to_delete = self.playlist.head
        if node_to_delete is None: return

        for _ in range(index):
            if node_to_delete.next:
                node_to_delete = node_to_delete.next
        
        song_to_delete = node_to_delete.song
        
        # Now, delete from both places
        del self.song_lookup_table[song_to_delete.song_id]
        self.playlist.delete_song(index) # This will print its own message

    # NEW METHOD
    def lookup_song(self, song_id):
        """Instant O(1) lookup for a song by its ID.
        Time Complexity: O(1)
        Space Complexity: O(1)"""
        return self.song_lookup_table.get(song_id, "Song not found.")

    def rate_song(self, song, rating):
        """Adds a song with a given rating to the BST."""
        print(f"Rating '{song.title}' as {rating} stars.")
        self.rating_tree.insert_song(song, rating)
    
    

    def play_song(self, song):
        """Simulates playing a song and adds it to the history stack."""
        print(f"Playing: {song.title}")
        self.playback_history.append(song) # 'append' is our stack 'push'

    def undo_last_play(self):
        """
        Takes the last played song from the history stack and adds it
        back to the playlist.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.playback_history:
            print("No songs in playback history to undo.")
            return

        last_song = self.playback_history.pop() # 'pop' removes the last item
        self.playlist.add_song(last_song)
        print(f"Undone: '{last_song.title}' has been re-added to the playlist.")

    # Caling the delete song function from the BSTNode class    
    def delete_rated_song(self, song_id, rating):
        """Deletes a song with a given rating from the BST."""
        self.rating_tree.delete_song(song_id, rating)

    # This method goes inside the PlayWiseEngine class
    def export_snapshot(self):
        """
        Gathers live stats from all components and returns them in a dictionary.
        """
        # 1. Top 5 longest songs
        all_songs = list(self.song_lookup_table.values())
        # Use a lambda function for a quick, one-off sort by duration
        longest_songs = sorted(all_songs, key=lambda song: song.duration, reverse=True)[:5]

        # 2. Most recently played songs
        # Reverse the list to show most recent first
        recent_plays = self.playback_history[::-1]

        # 3. Song count by rating
        rating_counts = self.rating_tree.get_rating_counts()

        snapshot = {
            "top_5_longest_songs": longest_songs,
            "most_recently_played": recent_plays,
            "song_count_by_rating": rating_counts
        }
        return snapshot

class BSTNode:
    """A node in the Binary Search Tree for song ratings."""
    def __init__(self, key):
        self.key = key          # The rating (e.g., 1, 2, 3, 4, 5)
        self.songs = []         # A list of songs with this rating
        self.left = None        # Pointer to the left child node (lower ratings)
        self.right = None       # Pointer to the right child node (higher ratings)

class RatingBST:
    """Manages the BST of song ratings."""
    def __init__(self):
        self.root = None

    def insert_song(self, song, rating):
        """Public method to insert a song into the BST.
        Time Complexity: O(log n)
        Space Complexity: O(log n)"""
        # This is a wrapper for the recursive insert function.
        self.root = self._insert(self.root, rating, song)

    def _insert(self, current_node, key, song):
        """Private recursive method to find the correct spot and insert."""
        # Base Case: If we've found an empty spot, create a new node.
        if current_node is None:
            new_node = BSTNode(key)
            new_node.songs.append(song)
            return new_node

        # Recursive Step:
        if key < current_node.key:
            current_node.left = self._insert(current_node.left, key, song)
        elif key > current_node.key:
            current_node.right = self._insert(current_node.right, key, song)
        else:
            # If key already exists, just add the song to the list.
            current_node.songs.append(song)
        
        return current_node
    
    # This method goes inside the RatingBST class
    def search_by_rating(self, rating):
        """Public method to search for songs with a specific rating.
        Time Complexity: O(log n)
        Space Complexity: O(log n)"""
        node = self._search(self.root, rating)
        if node:
            return node.songs
        return [] # Return an empty list if the rating is not found

    def _search(self, current_node, key):
        """Private recursive method to find the node with the matching key."""
        # Base Case 1: The rating does not exist in the tree.
        if current_node is None:
            return None
        
        # Base Case 2: We found the node with the matching rating.
        if current_node.key == key:
            return current_node
        
        # Recursive Step: Decide whether to go left or right.
        if key < current_node.key:
            return self._search(current_node.left, key)
        else: # key > current_node.key
            return self._search(current_node.right, key)
        
    # To Delete a song inside a particular rating bin 
    def delete_song(self, song_id, rating):
        """Finds the correct rating node and removes a specific song from its list.
        Time Complexity: O(log n)
        Space Complexity: O(1)"""
        # Step 1: Find the node with the given rating.
        node = self._search(self.root, rating)

        if node:
            # Step 2: Find the song with the matching ID in the node's list.
            song_to_delete = None
            for song in node.songs:
                if song.song_id == song_id:
                    song_to_delete = song
                    break
            
            # Step 3: Remove the song if it was found.
            if song_to_delete:
                node.songs.remove(song_to_delete)
                print(f"Deleted '{song_to_delete.title}' from rating {rating}.")
                # Optional: If the list becomes empty, you could decide to delete the tree node,
                # but for this project, leaving the empty node is fine.
            else:
                print(f"Error: Song ID {song_id} not found with rating {rating}.")
        else:
            print(f"Error: Rating {rating} not found in the tree.")

    def display(self):
        """A wrapper for the recursive in-order traversal print."""
        print("--- Song Ratings (In-Order) ---")
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, current_node):
        """Prints the tree's contents by visiting left, root, then right."""
        if current_node is not None:
            self._in_order_traversal(current_node.left)
            print(f"Rating {current_node.key} Stars: {current_node.songs}")
            self._in_order_traversal(current_node.right)

    # This method goes inside the RatingBST class
    def get_rating_counts(self):
        """Returns a dictionary of rating counts."""
        counts = {}
        self._collect_counts(self.root, counts)
        return counts

    def _collect_counts(self, current_node, counts):
        """Private recursive helper to collect song counts."""
        if current_node is not None:
            self._collect_counts(current_node.left, counts)
            counts[current_node.key] = len(current_node.songs)
            self._collect_counts(current_node.right, counts)
