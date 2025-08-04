# PlayWise: Technical Design Document

This document outlines the architecture and design choices for the PlayWise backend engine, a system designed for efficient playlist management and personalization.

---

## 1. High-Level Architecture

The system is designed around a central `PlayWiseEngine` class that acts as a manager for several specialized data structures. This encapsulates the logic and provides a clean interface for any future front-end application.

**Diagram:**

+------------------+
|   PlayWiseEngine |
|------------------|
| - playlist       |<>--+  Playlist (Doubly Linked List)
| - history_stack  |<>--+  Playback History (Stack)
| - rating_tree    |<>--+  Song Ratings (Binary Search Tree)
| - lookup_table   |<>--+  Instant Lookup (HashMap)
+------------------+

---

## 2. Data Structure & Algorithm Justification

### Doubly Linked List (Playlist)
* **Why:** A doubly linked list was chosen for the core playlist because it provides highly efficient `O(1)` insertions and deletions at the ends. More importantly, it allows for complex reordering operations like `move_song` by simply manipulating a few pointers, which is more efficient than using an array where moving an element would be `O(n)`.

### Stack (Playback History)
* **Why:** A stack is the ideal data structure for a "playback history" or "undo" feature due to its Last-In, First-Out (LIFO) behavior. The last song played is the first one accessed, which is exactly the required logic. Both push (`append`) and pop operations are `O(1)`.

### HashMap (Instant Song Lookup)
* **Why:** The requirement for an `O(1)` time lookup by a unique `song_id` points directly to using a HashMap (a Python dictionary). No other data structure provides this constant-time access, making it essential for features like an instant search bar.

### Binary Search Tree (Song Ratings)
* **Why:** To organize songs by a sortable key (the rating), a BST is a natural choice. It provides `O(log n)` average time complexity for searching, inserting, and deleting songs based on their rating, which is significantly more performant than a linear `O(n)` scan.

### Merge Sort (Playlist Sorting)
* **Why:** Merge Sort was chosen for its stable and predictable `O(n log n)` time complexity. Unlike Quick Sort, its worst-case performance is still `O(n log n)`, making it a reliable choice for sorting playlists by various criteria like title or duration.

---

## 3. Pseudocode for Major Algorithms


1. Doubly Linked List - Move Song
This algorithm shows the pointer manipulation required to move a node from one position to another.

FUNCTION move_song(from_index, to_index):
  // Find the node to move
  node_to_move = GET_NODE_AT(from_index)

  // Unlink the node from its current position
  IF node_to_move.prev is not NULL:
    node_to_move.prev.next = node_to_move.next
  ELSE:
    // It was the head
    playlist.head = node_to_move.next
  ENDIF

  IF node_to_move.next is not NULL:
    node_to_move.next.prev = node_to_move.prev
  ELSE:
    // It was the tail
    playlist.tail = node_to_move.prev
  ENDIF

  // Find the target node to insert before
  target_node = GET_NODE_AT(to_index)

  // Re-insert the node at the new position
  IF target_node is NULL:
    // Move to the end
    playlist.tail.next = node_to_move
    node_to_move.prev = playlist.tail
    playlist.tail = node_to_move
  ELSE:
    // Insert before target node
    node_to_move.prev = target_node.prev
    node_to_move.next = target_node
    IF target_node.prev is not NULL:
      target_node.prev.next = node_to_move
    ELSE:
      playlist.head = node_to_move
    ENDIF
    target_node.prev = node_to_move
  ENDIF
ENDFUNCTION

2. Binary Search Tree - Recursive Insert
This algorithm shows how a song is recursively placed into the correct rating bucket in the BST.

FUNCTION _insert(current_node, key, song):
  IF current_node is NULL:
    new_node = CREATE_NODE(key)
    ADD song to new_node.songs
    RETURN new_node
  ENDIF

  IF key < current_node.key:
    current_node.left = _insert(current_node.left, key, song)
  ELSE IF key > current_node.key:
    current_node.right = _insert(current_node.right, key, song)
  ELSE:
    // Key already exists, just add the song
    ADD song to current_node.songs
  ENDIF

  RETURN current_node
ENDFUNCTION

3. Merge Sort Algorithm
This algorithm shows the recursive "divide and conquer" logic for sorting.

FUNCTION _merge_sort(list_of_songs):
  IF length of list_of_songs <= 1:
    RETURN list_of_songs
  ENDIF

  // Divide
  mid = length of list_of_songs / 2
  left_half = _merge_sort(first half of list_of_songs)
  right_half = _merge_sort(second half of list_of_songs)

  // Combine
  RETURN merge(left_half, right_half)
ENDFUNCTION

FUNCTION merge(left_list, right_list):
  sorted_list = CREATE_EMPTY_LIST()
  WHILE left_list and right_list are not empty:
    IF first element of left_list < first element of right_list:
      MOVE first element of left_list to sorted_list
    ELSE:
      MOVE first element of right_list to sorted_list
    ENDIF
  ENDWHILE

  ADD any remaining elements from left_list to sorted_list
  ADD any remaining elements from right_list to sorted_list

  RETURN sorted_list
ENDFUNCTION


---

## 4. Test Case Results

This section shows the output from running the `main.py` script, demonstrating that all features are implemented and working correctly.

*My awesome playlist:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)
3. Hotel California by Eagles (390s)

Playlist(songs=3)

--- Testing Deletion ---
Deleted 'Stairway to Heaven' from the playlist.
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)

Playlist(songs=2)
Deleted 'Bohemian Rhapsody' from the playlist.
1. Hotel California by Eagles (390s)

--- Testing Move ---
Original Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Moving Song D (index 3) to index 0...
1. Song D by Art (100s)
2. Song A by Art (100s)
3. Song B by Art (100s)
4. Song C by Art (100s)

Moving Song A (index 1) to index 3...
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

--- Testing Reverse ---
Playlist before reverse:
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

Reversing the playlist...
Playlist has been reversed.

Playlist after reverse:
1. Song A by Art (100s)
2. Song C by Art (100s)
3. Song B by Art (100s)
4. Song D by Art (100s)
--- Testing Playback History ---
Initial Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Playing two songs...
Playing: Song A
Playing: Song B

Playback History (top of stack is last): [Song(Song A by Art), Song(Song B by Art)]

Undoing the last play...
Undone: 'Song B' has been re-added to the playlist.

New Playback History: [Song(Song A by Art)]
Playlist after undo:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)
5. Song B by Art (100s)

--- Testing Rating Tree ---
Rating 'Song C' as 5 stars.
Rating 'Song A' as 4 stars.
Rating 'Song B' as 5 stars.
Rating 'Song D' as 2 stars.
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

--- Testing Rating Search ---
Searching for 5-star songs...
Found: [Song(Song C by Art), Song(Song B by Art)]

Searching for 3-star songs...
Found: []
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine> ^C
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>  c:; cd 'c:\Users\vinst\OneDrive\Desktop\playwise_engine'; & 'c:\Users\vinst\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\vinst\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '56108' '--' 'C:\Users\vinst\OneDrive\Desktop\playwise_engine\main.py' 

My awesome playlist:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)
3. Hotel California by Eagles (390s)

Playlist(songs=3)

--- Testing Deletion ---
Deleted 'Stairway to Heaven' from the playlist.
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)

Playlist(songs=2)
Deleted 'Bohemian Rhapsody' from the playlist.
1. Hotel California by Eagles (390s)

--- Testing Move ---
Original Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Moving Song D (index 3) to index 0...
1. Song D by Art (100s)
2. Song A by Art (100s)
3. Song B by Art (100s)
4. Song C by Art (100s)

Moving Song A (index 1) to index 3...
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

--- Testing Reverse ---
Playlist before reverse:
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

Reversing the playlist...
Playlist has been reversed.

Playlist after reverse:
1. Song A by Art (100s)
2. Song C by Art (100s)
3. Song B by Art (100s)
4. Song D by Art (100s)
--- Testing Playback History ---
Initial Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Playing two songs...
Playing: Song A
Playing: Song B

Playback History (top of stack is last): [Song(Song A by Art), Song(Song B by Art)]

Undoing the last play...
Undone: 'Song B' has been re-added to the playlist.

New Playback History: [Song(Song A by Art)]
Playlist after undo:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)
5. Song B by Art (100s)

--- Testing Rating Tree ---
Rating 'Song C' as 5 stars.
Rating 'Song A' as 4 stars.
Rating 'Song B' as 5 stars.
Rating 'Song D' as 2 stars.
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

--- Testing Rating Search ---
Searching for 5-star songs...
Found: [Song(Song C by Art), Song(Song B by Art)]

Searching for 3-star songs...
Found: []

--- Testing Rating Deletion ---
Tree before deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

Deleting Song B (ID: S002, Rating: 5)...
Deleted 'Song B' from rating 5.

Tree after deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art)]
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine> ^C
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>  c:; cd 'c:\Users\vinst\OneDrive\Desktop\playwise_engine'; & 'c:\Users\vinst\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\vinst\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '56382' '--' 'C:\Users\vinst\OneDrive\Desktop\playwise_engine\main.py' 

My awesome playlist:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)
3. Hotel California by Eagles (390s)

Playlist(songs=3)

--- Testing Deletion ---
Deleted 'Stairway to Heaven' from the playlist.
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)

Playlist(songs=2)
Deleted 'Bohemian Rhapsody' from the playlist.
1. Hotel California by Eagles (390s)

--- Testing Move ---
Original Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Moving Song D (index 3) to index 0...
1. Song D by Art (100s)
2. Song A by Art (100s)
3. Song B by Art (100s)
4. Song C by Art (100s)

Moving Song A (index 1) to index 3...
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

--- Testing Reverse ---
Playlist before reverse:
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

Reversing the playlist...
Playlist has been reversed.

Playlist after reverse:
1. Song A by Art (100s)
2. Song C by Art (100s)
3. Song B by Art (100s)
4. Song D by Art (100s)
--- Testing Playback History ---
Initial Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Playing two songs...
Playing: Song A
Playing: Song B

Playback History (top of stack is last): [Song(Song A by Art), Song(Song B by Art)]

Undoing the last play...
Undone: 'Song B' has been re-added to the playlist.

New Playback History: [Song(Song A by Art)]
Playlist after undo:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)
5. Song B by Art (100s)

--- Testing Rating Tree ---
Rating 'Song C' as 5 stars.
Rating 'Song A' as 4 stars.
Rating 'Song B' as 5 stars.
Rating 'Song D' as 2 stars.
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

--- Testing Rating Search ---
Searching for 5-star songs...
Found: [Song(Song C by Art), Song(Song B by Art)]

Searching for 3-star songs...
Found: []

--- Testing Rating Deletion ---
Tree before deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

Deleting Song B (ID: S002, Rating: 5)...
Deleted 'Song B' from rating 5.

Tree after deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art)]
Added 'Bohemian Rhapsody' to playlist and lookup table.
Added 'Stairway to Heaven' to playlist and lookup table.

--- Testing Instant Lookup ---
Playlist contents:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)

Looking up song S002...
Found: Song(Stairway to Heaven by Led Zeppelin)
Its duration is: 482s

Deleting song at index 0...
Deleted 'Bohemian Rhapsody' from the playlist.

Looking up song S001 (should be gone)...
Found: Song not found.
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine> ^C
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>  c:; cd 'c:\Users\vinst\OneDrive\Desktop\playwise_engine'; & 'c:\Users\vinst\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\vinst\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '56556' '--' 'C:\Users\vinst\OneDrive\Desktop\playwise_engine\main.py' 

My awesome playlist:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)
3. Hotel California by Eagles (390s)

Playlist(songs=3)

--- Testing Deletion ---
Deleted 'Stairway to Heaven' from the playlist.
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)

Playlist(songs=2)
Deleted 'Bohemian Rhapsody' from the playlist.
1. Hotel California by Eagles (390s)

--- Testing Move ---
Original Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Moving Song D (index 3) to index 0...
1. Song D by Art (100s)
2. Song A by Art (100s)
3. Song B by Art (100s)
4. Song C by Art (100s)

Moving Song A (index 1) to index 3...
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

--- Testing Reverse ---
Playlist before reverse:
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

Reversing the playlist...
Playlist has been reversed.

Playlist after reverse:
1. Song A by Art (100s)
2. Song C by Art (100s)
3. Song B by Art (100s)
4. Song D by Art (100s)
--- Testing Playback History ---
Initial Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Playing two songs...
Playing: Song A
Playing: Song B

Playback History (top of stack is last): [Song(Song A by Art), Song(Song B by Art)]

Undoing the last play...
Undone: 'Song B' has been re-added to the playlist.

New Playback History: [Song(Song A by Art)]
Playlist after undo:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)
5. Song B by Art (100s)

--- Testing Rating Tree ---
Rating 'Song C' as 5 stars.
Rating 'Song A' as 4 stars.
Rating 'Song B' as 5 stars.
Rating 'Song D' as 2 stars.
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

--- Testing Rating Search ---
Searching for 5-star songs...
Found: [Song(Song C by Art), Song(Song B by Art)]

Searching for 3-star songs...
Found: []

--- Testing Rating Deletion ---
Tree before deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

Deleting Song B (ID: S002, Rating: 5)...
Deleted 'Song B' from rating 5.

Tree after deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art)]
Added 'Bohemian Rhapsody' to playlist and lookup table.
Added 'Stairway to Heaven' to playlist and lookup table.

--- Testing Instant Lookup ---
Playlist contents:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)

Looking up song S002...
Found: Song(Stairway to Heaven by Led Zeppelin)
Its duration is: 482s

Deleting song at index 0...
Deleted 'Bohemian Rhapsody' from the playlist.

Looking up song S001 (should be gone)...
Found: Song not found.

--- Testing Sorting ---
Added 'Hotel California' to playlist and lookup table.
Added 'Bohemian Rhapsody' to playlist and lookup table.
Added 'Stairway to Heaven' to playlist and lookup table.
Original playlist:
1. Hotel California by Eagles (390s)
2. Bohemian Rhapsody by Queen (355s)
3. Stairway to Heaven by Led Zeppelin (482s)

Sorting by title...
Playlist sorted by title (asc).
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)
3. Stairway to Heaven by Led Zeppelin (482s)

Sorting by duration (descending)...
Playlist sorted by duration (desc).
1. Stairway to Heaven by Led Zeppelin (482s)
2. Hotel California by Eagles (390s)
3. Bohemian Rhapsody by Queen (355s)
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine> ^C
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>
PS C:\Users\vinst\OneDrive\Desktop\playwise_engine>  c:; cd 'c:\Users\vinst\OneDrive\Desktop\playwise_engine'; & 'c:\Users\vinst\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\vinst\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '57400' '--' 'C:\Users\vinst\OneDrive\Desktop\playwise_engine\main.py' 

My awesome playlist:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)
3. Hotel California by Eagles (390s)

Playlist(songs=3)

--- Testing Deletion ---
Deleted 'Stairway to Heaven' from the playlist.
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)

Playlist(songs=2)
Deleted 'Bohemian Rhapsody' from the playlist.
1. Hotel California by Eagles (390s)

--- Testing Move ---
Original Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Moving Song D (index 3) to index 0...
1. Song D by Art (100s)
2. Song A by Art (100s)
3. Song B by Art (100s)
4. Song C by Art (100s)

Moving Song A (index 1) to index 3...
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

--- Testing Reverse ---
Playlist before reverse:
1. Song D by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song A by Art (100s)

Reversing the playlist...
Playlist has been reversed.

Playlist after reverse:
1. Song A by Art (100s)
2. Song C by Art (100s)
3. Song B by Art (100s)
4. Song D by Art (100s)
--- Testing Playback History ---
Initial Playlist:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)

Playing two songs...
Playing: Song A
Playing: Song B

Playback History (top of stack is last): [Song(Song A by Art), Song(Song B by Art)]

Undoing the last play...
Undone: 'Song B' has been re-added to the playlist.

New Playback History: [Song(Song A by Art)]
Playlist after undo:
1. Song A by Art (100s)
2. Song B by Art (100s)
3. Song C by Art (100s)
4. Song D by Art (100s)
5. Song B by Art (100s)

--- Testing Rating Tree ---
Rating 'Song C' as 5 stars.
Rating 'Song A' as 4 stars.
Rating 'Song B' as 5 stars.
Rating 'Song D' as 2 stars.
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

--- Testing Rating Search ---
Searching for 5-star songs...
Found: [Song(Song C by Art), Song(Song B by Art)]

Searching for 3-star songs...
Found: []

--- Testing Rating Deletion ---
Tree before deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art), Song(Song B by Art)]

Deleting Song B (ID: S002, Rating: 5)...
Deleted 'Song B' from rating 5.

Tree after deletion:
--- Song Ratings (In-Order) ---
Rating 2 Stars: [Song(Song D by Art)]
Rating 4 Stars: [Song(Song A by Art)]
Rating 5 Stars: [Song(Song C by Art)]
Added 'Bohemian Rhapsody' to playlist and lookup table.
Added 'Stairway to Heaven' to playlist and lookup table.

--- Testing Instant Lookup ---
Playlist contents:
1. Bohemian Rhapsody by Queen (355s)
2. Stairway to Heaven by Led Zeppelin (482s)

Looking up song S002...
Found: Song(Stairway to Heaven by Led Zeppelin)
Its duration is: 482s

Deleting song at index 0...
Deleted 'Bohemian Rhapsody' from the playlist.

Looking up song S001 (should be gone)...
Found: Song not found.

--- Testing Sorting ---
Added 'Hotel California' to playlist and lookup table.
Added 'Bohemian Rhapsody' to playlist and lookup table.
Added 'Stairway to Heaven' to playlist and lookup table.
Original playlist:
1. Hotel California by Eagles (390s)
2. Bohemian Rhapsody by Queen (355s)
3. Stairway to Heaven by Led Zeppelin (482s)

Sorting by title...
Playlist sorted by title (asc).
1. Bohemian Rhapsody by Queen (355s)
2. Hotel California by Eagles (390s)
3. Stairway to Heaven by Led Zeppelin (482s)

Sorting by duration (descending)...
Playlist sorted by duration (desc).
1. Stairway to Heaven by Led Zeppelin (482s)
2. Hotel California by Eagles (390s)
3. Bohemian Rhapsody by Queen (355s)

--- Testing System Snapshot ---
Playing: Stairway to Heaven
Playing: Hotel California
{
    "top_5_longest_songs": [
        {
            "song_id": "S002",
            "title": "Stairway to Heaven",
            "artist": "Led Zeppelin",
            "duration": 482
        },
        {
            "song_id": "S003",
            "title": "Hotel California",
            "artist": "Eagles",
            "duration": 390
        },
        {
            "song_id": "S001",
            "title": "Bohemian Rhapsody",
            "artist": "Queen",
            "duration": 355
        }
    ],
    "most_recently_played": [
        {
            "song_id": "S003",
            "title": "Hotel California",
            "artist": "Eagles",
            "duration": 390
        },
        {
            "song_id": "S002",
            "title": "Stairway to Heaven",
            "artist": "Led Zeppelin",
            "duration": 482
        }
    ],
    "song_count_by_rating": {}
}*

