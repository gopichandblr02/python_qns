### 🟩 CORE PYTHON DATA STRUCTURES

#### These are built-in and used everywhere.

**1. List (Dynamic Array)**

Python’s list = dynamic array.

* Operations + Big-O
* Operation	Big-O
* Access by index	O(1)
* Append at end	O(1) amortized
* Insert at beginning	O(n)
* Insert at middle	O(n)
* Delete by index	O(n)
* Search (linear)	O(n)
* Pop end	O(1)
Visual:
[10, 20, 30, 40]

**2. Tuple**

Immutable list.

* Operation	Big-O
* Access	O(1)
* Search	O(n)
* Immutable → no insert/delete	—

Used for fixed collections, hash keys.

**3. Set (Hash Set)**

Unordered, unique elements.

* Operation	Big-O
* Add	O(1) average
* Remove	O(1)
* Search	O(1)
* Iterate	O(n)

**4. Dict (Hash Map)**

Key → Value mapping.

* Operation	Big-O
* Insert	O(1)
* Delete	O(1)
* Search	O(1)
* Access value	O(1)

**5. String**

Immutable sequence.

Operation	Big-O
Access	O(1)
Search substring	O(n)
Concatenation	O(n)

### 🟦 ADVANCED PYTHON DATA STRUCTURES

These come from modules like collections, heapq, queue.

**1. deque (Double-ended queue) — from collections**

Best for FIFO queues and both-side operations.

* Operation	Big-O
* append()	O(1)
* appendleft()	O(1)
* pop()	O(1)
* popleft()	O(1)

**2. heapq (Binary Min Heap)**

Python uses min-heap.

Operation	Big-O
push	O(log n)
pop	O(log n)
peek (heap[0])	O(1)

Used in:

Kth largest

Priority queues

Dijkstra

3. Queue — from queue module

Thread-safe queue.

Type	Use
Queue	FIFO
LifoQueue	stack
PriorityQueue	min-heap

Each operation is usually O(1).

4. Linked Lists (Manual Class Implementations)

Big-O (singly/doubly):

Operation	Singly	Doubly
Access	O(n)	O(n)
Insert head	O(1)	O(1)
Insert tail	O(n)	O(1) if tail pointer
Delete	O(n)	O(n)
Search	O(n)	O(n)

**5. Stack**

Using list or deque.

Operation	Big-O
push	O(1)
pop	O(1)
peek	O(1)

**6. OrderedDict**

Maintains insertion order (now default in Python 3.7+).

**7. Counter**

Hash map with counts.

Operation	Big-O
Count items	O(n)
Access count	O(1)
🟥 BIG-O CHEATSHEET (INTERVIEW READY)
Time Complexity Rankings

Fastest → Slowest:

O(1)  → O(log n) → O(n) → O(n log n) → O(n²) → O(2^n) → O(n!)

**Common Algorithm Complexities**
Task	Best DS	Complexity
Search unsorted	list	O(n)
Search sorted	binary search	O(log n)
Find max/min	list	O(n)
Sort	built-in sort()	O(n log n)
Insert at end	list	O(1)
BFS/DFS	graph	O(V + E)
Hash lookup	dict or set	O(1)
**⭐ Sorting Algorithms**
Algorithm	Time Avg	Space
QuickSort	O(n log n)	O(log n)
MergeSort	O(n log n)	O(n)
HeapSort	O(n log n)	O(1)
BubbleSort	O(n²)	O(1)
InsertionSort	O(n²)	O(1)

**⭐ Data Structure Big-O Summary Table**

+------------------+----------+----------+----------+-------+
| Data Structure   | Access   | Search   | Insert   | Delete|
+------------------+----------+----------+----------+-------+
| Array/List       | O(1)     | O(n)     | O(n)     | O(n)  |
| Linked List      | O(n)     | O(n)     | O(1)     | O(1)* |
| Stack            | O(1)     | O(n)     | O(1)     | O(1)  |
| Queue            | O(1)     | O(n)     | O(1)     | O(1)  |
| Hash Map (dict)  | O(1)     | O(1)     | O(1)     | O(1)  |
| Set              | O(1)     | O(1)     | O(1)     | O(1)  |
| Heap             | O(n)     | O(n)     | O(log n) | O(log n) |
+------------------+----------+----------+----------+-------+


*for linked list delete = O(1) only if you already have the node reference.



The primary difference between a list (usually implemented as a dynamic array) and a linked list lies in their underlying memory management and how elements are connected, which leads to different performance trade-offs. List (Dynamic Array): Elements are stored in a single, contiguous block of memory and accessed by an index.Linked List: Elements (nodes) can be stored anywhere in memory and are connected by pointers or references to the next (and sometimes previous) node in the sequence. Key Distinctions Feature List (Dynamic Array, e.g., Python list, Java ArrayList)Linked List (e.g., Java LinkedList)Memory StorageContiguous (adjacent memory addresses)Non-contiguous (scattered in memory, linked by pointers)Random Access (by index)Fast (Constant Time: O(1)) because the memory address can be calculated directlySlow (Linear Time: O(n)) because you must traverse the list from the beginning to find the \(n\)-th elementInsertion/Deletion (Middle/Beginning)Slow (Linear Time: O(n)) because subsequent elements must be shifted to fill the gap or make roomFast (Constant Time: O(1)) if you have a reference to the adjacent node, as only pointers need to be updatedMemory OverheadLower (only stores data)Higher (each node stores data + one or two pointers)Size FlexibilityDynamic, but resizing can be an expensive operation that involves allocating a new, larger block of memory and copying all elements (amortized constant time for appends)Inherently dynamic; grows and shrinks easily at runtime without massive memory reallocationCache PerformanceGood (better cache locality due to contiguous memory)Poor (elements can be scattered, leading to more cache misses)When to Use Which Use a List/Dynamic Array when:You need frequent and fast random access to elements by index (e.g., list[5]).You know the size of the collection in advance or the list does not change size frequently.You are iterating through all elements sequentially and performance is critical (due to cache efficiency).Use a Linked List when:You need frequent insertions or deletions of elements, especially at the beginning or middle of the list.The size of the list is highly variable and unpredictable.You primarily access elements sequentially (using an iterator to traverse the list) rather than by a specific index.  Creating a public link...