
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