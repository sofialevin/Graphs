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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error adding edge. Vertex not found.")   

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set([starting_vertex])
        queue = Queue()

        # Enqueue starting vertex (root of traversal)
        queue.enqueue(starting_vertex)

        # Continue until queue is empty (meaning the whole graph has been traversed)
        while queue.size() != 0:
            # Peek queue head
            current_vertex = queue.dequeue()
            # Enqueue connected vertices
            for vertex in self.vertices[current_vertex]:
                if vertex not in visited:
                    # Add to queue if not already visited
                    queue.enqueue(vertex)
                    # Set as visited to prevent further enqueueing of same vertex
                    visited.add(vertex)

            # Do work on current vertex
            print(current_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Setup
        visited = set([starting_vertex])
        stack = Stack()
        # Put root on top of stack
        stack.push(starting_vertex)

        while stack.size() > 0:
            # Pointer to current vertex
            current_vertex = stack.pop()

            for vertex in self.vertices[current_vertex]:
                if vertex not in visited:
                    # Push vertex
                    stack.push(vertex)
                    # Mark visited
                    visited.add(vertex)

            # Do work on vertex
            print(current_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Setup
        visited = set([starting_vertex])
        
        def dive(current_vertex, visited):
            
            # Do work on vertex
            print(current_vertex)

            # Go thru neighbors and dive if not visited
            for vertex in self.get_neighbors(current_vertex):
                if vertex not in visited:
                    # Mark visited
                    visited.add(vertex)
                    # DIVE!!!
                    dive(vertex, visited)

        # Start recursion
        dive(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Previously visited nodes
        visited = set()

        queue = Queue()

        # Enqueue starting vertex (start of search)
        queue.enqueue([starting_vertex])

        # Continue until queue is empty (meaning the destination wasn't found)
        # OR we return a valid path
        while queue.size() != 0:
            # Get path
            path = queue.dequeue()
            # We want to find neighbors of last appended vertex
            current_vertex = path[-1]

            # Check if destination reached
            if current_vertex == destination_vertex:
                # Return shortest path
                return path
            else:
                # Check if visited
                if current_vertex not in visited:
                    # Don't wanna get stuck in a forever looping cycle
                    visited.add(current_vertex)
                    # Go thru neighbors
                    for vertex in self.get_neighbors(current_vertex):
                        if vertex not in visited:
                            # Build a new path from previous path, and add this vertex
                            new_path = path.copy()
                            new_path.append(vertex)
                            # Add to queue for processing in next iteration
                            queue.enqueue(new_path)
        # No path found case
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()

        stack = Stack()

        # push starting vertex (start of search)
        stack.push([starting_vertex])

        # Continue until stack is empty (meaning the destination wasn't found)
        # OR we return a valid path
        while stack.size() != 0:
            # Get path from stack
            path = stack.pop()
            # We want to find neighbors of last appended vertex
            current_vertex = path[-1]

            # Check if destination reached
            if current_vertex == destination_vertex:
                # Return shortest path
                return path
            else:
                # Check if visited
                if current_vertex not in visited:
                    # Don't wanna get stuck in a forever looping cycle
                    visited.add(current_vertex)
                    # Go thru neighbors
                    for vertex in self.get_neighbors(current_vertex):
                        if vertex not in visited:
                            # Build a new path from previous path, and add this vertex
                            new_path = path.copy()
                            new_path.append(vertex)
                            # Add to stack for processing in next iteration
                            stack.push(new_path)
        # No path found case
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Setup
        visited = set()

        # Recursion helper
        def dive(current_vertex, destination_vertex, visited):
            if current_vertex in visited:
                # Don't repeat work
                return None
            elif current_vertex == destination_vertex:
                # Base case -> reached destination_vertex
                return [destination_vertex]
            else:
                # Build path
                visited.add(current_vertex)
                # Go thru neighbors
                for vertex in self.get_neighbors(current_vertex):
                    # Recurse with current vertex as starting point
                    search = dive(vertex, destination_vertex, visited)
                    # When search ends up finding the destination, return starting_vertex + search path
                    if search is not None:
                        return [current_vertex] + search

                # No neighbors for node + search found nothing
                return None

        # Start recursion and return result
        return dive(starting_vertex, destination_vertex, visited)

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
