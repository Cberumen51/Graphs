"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #  TODO
        # create the new key with the vertex ID, and set the falue to an empty set (meaing no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        # find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
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
           

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex 
        s = Stack()
        s.push(starting_vertex)
        # Create an empty set to track visited verticies
        visited = set()
        # while the stack is not empty:
        while s.size() > 0:
            # get current vertex (pop from stack)
            current_vertex = s.pop()
            # Check if the current vertex has not been visited:
            if current_vertex not in visited:
                # print the current vertex
                print(current_vertex)
                # Mark the current vertex as visited
                # Add the current vertex to a visited_set
                visited.add(current_vertex)
                # push up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(current_vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # init visited as set
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                else:
                    # Mark as visited
                    visited.add(last_vert)
                    # Then add A PATH TO its neighbors to the back of the queue
                    for edge in self.get_neighbors(last_vert):
                        # copy path
                        path_copy = list(path)
                        # append neighbor to th back
                        path_copy.append(edge)
                        q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        queue = Queue()
        visited = set()
        # Create an empty set to track visited verticies
        queue.enqueue({
            "current_vertex": starting_vertex,
            "path": [starting_vertex]
        })
        # while the queue is not empty:
        while queue.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']
            # set the current vertex to the LAST element of the PATH

            # check if the current vertex has not been visited:
            if current_vertex not in visited:

                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, TOP AND RETURN
                if current_vertex == destination_vertex:
                    return current_path

                # Mark the current veretx as visited                    
                # add the current veretx to a visited_set

                visited.add(current_vertex)
                
                for neighbor_vertex in self.get_neighbors(current_vertex):
                # Queue up NEW paths with each nieghbor:
                    # take current path
                    # append the neightbor to it
                    # queue up NEW path
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })
        # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
