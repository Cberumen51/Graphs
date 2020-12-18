
  
class Queue():
    def __init__(self):
        # create empty queue
        self.queue = []
    # enqueue starting
    def enqueue(self, value):
        self.queue.append(value)
    # while queue is not empty dequeue from queue else return nonoe
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    # finding the size of the queue
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with teh vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while q.size() > 0:
            # get current vertex (dequeue from queue)
            current_vertex = q.dequeue()
            # Check if the current vertex has not been visited:
            if current_vertex not in visited:
                # print the current vertex
                print(current_vertex)
                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited.add(current_vertex)
                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(current_vertex):
                    q.enqueue(neighbor)

def earliest_ancestor(ancestors, starting_node):

    graph = Graph()
    # set up graph
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])

    # do BFS
    # create a queue
    q = Queue()
    # add start word to Queue (like a path)
    q.enqueue([starting_node])
    # create a visited set
    visited = set()

    # If the input individual has no parents, the function should return -1.
    ancestor = -1

    # while queue not empty
    while q.size() > 0:
        # pop current path off queue
        current_path = q.dequeue()
        current_node = current_path[-1]

        # if current node has not been visited:
        if current_node not in visited:
            # add current node
            visited.add(current_node)

            # See if the current node is less than the parent then
            if (current_node < ancestor) or (len(current_path) > 1):
                # set the parent as the current node
                ancestor = current_node

            # Check for the neighbors of the current_node
            for neighbor in graph.get_neighbors(current_node):
                # copy the path
                new_path = current_path.copy()
                # add the neighbor to the path
                new_path.append(neighbor)
                # and add the path to the queue
                q.enqueue(new_path)

    return ancestor