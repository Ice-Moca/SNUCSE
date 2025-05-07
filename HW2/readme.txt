Name: 여은수  
Student ID: 2023-12753  
Assignment Number: 2

Description:
With searching the algorithms of SCC, I found that the algorithm shown in the ppt 11 is Kosaraju's Algorithm.
So in hw2.py, I tried to implement Kosaraju's algorithm to find strongly connected components in a directed graph.
Also, I tried to make the commands similar to the format written in HW2_specification.pdf.

It supports three representations:
* `-m`: adjacency matrix
* `-l`: adjacency list
* `-a`: adjacency array

Environment:
Tested on Linux Ubuntu environment

Usage:
python3 hw2.py [-m|-l|-a] < input.txt > output.txt
(you can change the name of input.txt and output.txt)

Run with adjacency matrix graph format
python3 hw2.py -m < input.txt > output.txt

Run with adjacency list graph format
python3 hw2.py -l < input.txt > output.txt

Run with adjacency array graph format
python3 hw2.py -a < input.txt > output.txt


Implementation Details:

1. Parse input and build both the forward and reverse graph representations outside the timed section.
2. Call `kosaraju_strongly_connected_components(...)` (which performs the two DFS passes) inside the timed section:

   ```python
   start = time.perf_counter()
   sccs = kosaraju_strongly_connected_components(...)
   end = time.perf_counter()
   ```
3. After timing, sort each SCC's vertices in ascending order, then sort the list of SCCs lexicographically.
4. Print each SCC on its own line, followed by the elapsed time `(end - start) * 1000` in milliseconds.

Implementation Note (Python specifics):

Due to Python's lack of raw pointer support, the adjacency list is implemented as a list of lists, where each djacency_lis[i] is itself a Python list of neighbors.

To represent the adjacency array I used two arrays, prefix_degree and adjacency_array.  
prefix_degree marks the index of the edge array containing vertex i's neighbors.
Form this index information we can get the vertex that is adjacent to the given vertex from adjacency_array.

The finner details about each functions are written in the code itself.