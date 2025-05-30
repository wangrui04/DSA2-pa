# PA1 Skeleton Code
# DSA2, spring 2025
# Name: Rui Wang
# Computing ID: bxe5fd
# Resources used: https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php#:~:text=Dijkstra's%20algorithm%20finds%20the%20shortest,all%20the%20unvisited%20neighboring%20vertices.
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
# https://www.geeksforgeeks.org/adjacency-list-in-python/

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.
import heapq
from enum import unique

# Read in the values for the number of side roads, main roads, and highways
[s,m,h] = [int(x) for x in input().split(" ")]
# Read in the side road edges
tmp = input().split(" ")
side_road_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*s,5)])
# Read in the main road edges
tmp = input().split(" ")
main_road_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*m,5)])
# Read in the highway edges
tmp = input().split(" ")
highway_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*h,5)])
# Read in how many test cases there will be
num_test_cases = int(input())
# Read in each test case
test_cases = []
for _ in range(num_test_cases):
	tmp = input().split(" ")
	test_cases.append((int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])))

# Generate a list of the nodes fron the edges read in
side_road_nodes = []
main_road_nodes = []
highway_nodes = []
all_nodes = []
for (x1,y1,x2,y2,w) in side_road_edges:
	side_road_nodes.append((x1,y1))
	side_road_nodes.append((x2,y2))
side_road_nodes = sorted(list(set(side_road_nodes))) # remove duplicates
for (x1,y1,x2,y2,w) in main_road_edges:
	main_road_nodes.append((x1,y1))
	main_road_nodes.append((x2,y2))
main_road_nodes = sorted(list(set(main_road_nodes))) # remove duplicates
for (x1,y1,x2,y2,w) in highway_edges:
	highway_nodes.append((x1,y1))
	highway_nodes.append((x2,y2))
highway_nodes = sorted(list(set(highway_nodes))) # remove duplicates
all_nodes = sorted(list(set(side_road_nodes+main_road_nodes+highway_nodes))) # combine and remove duplicates

# At this point, the data structures are as follows.  You may not need all of
# these in your code.
#
# - `s`, `m`, and `h` contain the (integer) number of side road edges, main
#   road edges, and highway edges, respectively
#
# - Edge data structures:
#   - `side_road_edges` contains a list of 5-tuples that represent the edges
#     of the side roads.  Example: [(0, 0, 0, 1, 1), (0, 0, 1, 0, 1), ...].
#     The 5-tuple is (x1,y1,x2,y2,2), where (x1,y1) is one end of the edge,
#     (x2,y2) is the other end, and w is the weight of the edge.  All values
#     are integers.  This list is sorted.  Note that this only has the edges
#     in one direction, but they are bi-directional edges.
#   - `main_road_edges` has the edges for the main roads, in the same form as
#     the edges for the side roads
#   - `highway_edges` has the edges for the main roads, in the same form as
#     the edges for the side roads
#
# - Node data structures:
#   - `side_road_nodes` contain all the nodes that connect to a side road as a
#     list of 2-tuples; this list is sorted
#   - `main_road_nodes` contain all the nodes that connect to a main road as a
#     list of 2-tuples; this list is sorted
#   - `highway_nodes` contain all the nodes that connect to a highway as a
#     list of 2-tuples; this list is sorted
#   - `all_nodes` contain all the nodes in the graph as a list of 2-tuples;
#     this list is sorted
#
# - Test case data structures:
#   - `num_test_cases` is how many test cases there are
#   - `test_cases` is the test cases themselves, as a list of 4-tuples.
#     Example: [(4, 0, 3, 8), (1, 1, 3, 7), (5, 1, 8, 3)].  Each tuple is of
#     the form (x1,y1,x2,y2), which means that the test case is to find the
#     route from (x1,y1) to (x2,y2).  The tuples in this list are in the
#     order they occur in the input file.


# output() function -- given a list of coordinates (as 2-tuples) and the
# (integer) distance, this function will output the result in the correct
# format for the auto-grader
def output(path,dist):
	print(dist)
	print(len(path))
	for (x,y) in path:
		print(x,y)
	print()



# YOUR CODE HERE
class Graph:
	def __init__(self, side_road_edges, main_road_edges, highway_edges, all_nodes, side_road_nodes, main_road_nodes, highway_nodes):
		self.side_road_nodes = set(side_road_nodes)
		self.main_road_nodes = set(main_road_nodes)
		self.highway_nodes = set(highway_nodes)

		self.graph = {node: [] for node in all_nodes}
		# need a different graph for each type of road

		# need an instance to represent the weight between the nodes
		# add side road to graph
		# find index, make list based on index
		# break down test input to output a tuple, essentially (x1, x2) or (y1, y2)
		for (x1, y1, x2, y2, w) in side_road_edges:
			self.graph[(x1, y1)].append(((x2, y2), w)) #when accessing and verifying, have to check first tuple against coordinate
			self.graph[(x2, y2)].append(((x1, y1), w)) #function of a tuple of 2 inputs

		# add main road to graph
		for (x1, y1, x2, y2, w) in main_road_edges:
			self.graph[(x1, y1)].append(((x2, y2), w))
			self.graph[(x2, y2)].append(((x1, y1), w))

		# add highway to graph
		for (x1, y1, x2, y2, w) in highway_edges:
			self.graph[(x1, y1)].append(((x2, y2), w))
			self.graph[(x2, y2)].append(((x1, y1), w))

	def dijkstra_algo(self, start, targets):
		#print(f"Running Dijkstra from {start} to {targets}")
		# everything starts at infinity unless i call "decreaseKey"
		distances = {node: float('inf') for node in self.graph}
		# at first node distance is 0
		distances[start] = 0

		# initialise parent for each node and they're all none initially
		parents = {node: None for node in self.graph}

		# min heap pq
		pq = [(0, start)]
		#heapq.heappush(pq, (0, start)) # distance, node

		while pq:
			# extractMin
			curr_dist, curr_node = heapq.heappop(pq)

			if curr_node in targets:
				return curr_node, distances[curr_node], parents

			for neighbour, weight in self.graph[curr_node]:
				new_dist = curr_dist + weight
				if new_dist < distances[neighbour]:
					distances[neighbour] = new_dist
					parents[neighbour] = curr_node
					# add neighbour to pq with updated dist
					heapq.heappush(pq, (new_dist, neighbour))

		# return curr_node, distances[curr_node], parents
		return None, float('inf'), parents

	def find_path(self, start, end):
		#path = []
		total_distance = 0

		# path 1 start on side road find nearest main road
		curr_node = start
		if curr_node not in self.main_road_nodes:
			curr_node, dist, parents1 = self.dijkstra_algo(start, self.main_road_nodes)
			if curr_node is None:  # no path to main road
				return [], float('inf')
			total_distance += dist
			path1 = self.construct_path(start, curr_node, parents1)
		else:
			path1 = []

		main_road_node_A = curr_node

		# path 2 from main road find nearest highway
		if main_road_node_A not in self.highway_nodes:
			curr_node, dist, parents2 = self.dijkstra_algo(main_road_node_A, self.highway_nodes)
			if curr_node is None:  # no path to highway
				return [], float('inf')
			# if new_node: # checks if we're at a new node
			total_distance += dist
			path2 = self.construct_path(main_road_node_A, curr_node, parents2)
		else:
			path2 = []
		highway_node_A = curr_node

		# path 3 from end node, side roads to the nearest main road
		curr_node = end
		if curr_node not in self.highway_nodes:
			curr_node, dist, parents3 = self.dijkstra_algo(end, self.main_road_nodes)
			if curr_node is None:
				return [], float('inf')
			total_distance += dist
			path3 = self.construct_path(end, curr_node, parents3)[::-1]
		else:
			path3 = []
		main_road_node_B = curr_node

		# path 4 from the main road node found in path 3, to the nearest highway
		if main_road_node_B not in self.highway_nodes:
			curr_node, dist, parents4 = self.dijkstra_algo(main_road_node_B, self.highway_nodes)
			if curr_node is None:
				return [], float('inf')
			total_distance += dist
			path4 = self.construct_path(main_road_node_B, curr_node, parents4)[::-1]
		else:
			path4 = []
		highway_node_B = curr_node

		# path 5 connect highway nodes A and B
		if highway_node_B == highway_node_A:
			path5 = []
		else:
			_, dist, parents5 = self.dijkstra_algo(highway_node_B, {highway_node_A})
			if parents5 is None:
				return [], float('inf')
			total_distance += dist
			path5 = self.construct_path(highway_node_B, highway_node_A, parents5)[::-1]

		# print(f"Path1: {path1}")
		# print(f"Path2: {path2}")
		# print(f"Path3: {path3}")
		# print(f"Path4: {path4}")
		# print(f"Path5: {path5}")
		path = path1 + path2 + path5 + path4 + path3

		seen = set()
		unique_path = []
		for node in path:
			if node not in seen:
				unique_path.append(node)
				seen.add(node)

		#total_distance = dist1 + dist2 + dist3 + dist4 + dist5

		return unique_path, total_distance

	def construct_path(self, start, end, parents):
		path = []
		current = end

		if start == end:
			return [start]

		while current is not None and current != start:
			path.append(current)
			#print(f"Tracing back: {current} -> {parents[current]}")
			current = parents.get(current, None)

		path.append(start)
		path.reverse()
		return path


#graph = Graph(side_road_edges, main_road_edges, highway_edges, all_nodes, side_road_nodes, main_road_nodes, highway_nodes)

for (x1, y1, x2, y2) in test_cases:
	#print(f"Processing test case: {(x1, y1)} -> {(x2, y2)}")
	graph = Graph(side_road_edges, main_road_edges, highway_edges, all_nodes, side_road_nodes, main_road_nodes, highway_nodes)
	path, distance = graph.find_path((x1, y1), (x2, y2))
	output(path, distance)

	# path is gonna be a list of tuples, wanna return the list that is the path then the int thats the distance