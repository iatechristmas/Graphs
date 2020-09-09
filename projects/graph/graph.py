"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.array_list = Stack()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # for holding edges
        self.vertices[vertex_id] = set() 

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 to the set if there's an edge from v1 to v2
            self.vertices[v1].add(v2)

        else:
            print("Error, nonexistant vert")

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
        # empty queue
        q = Queue()

        # set to store visited nodes

        visited = set()

        # enqueue starting node

        q.enqueue(starting_vertex)

        # while queue not empty
        while q.size():
            v = q.dequeue()

            # if it hasn't been visited
            if v not in visited:
                # mark as visited
                visited.add(v)

                #print node
                print(f"{v}")

                # add neighbors to queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # empty stack
        s = Stack()

        # set to store visited nodes
        visited = set()

        # push starting node
        s.push(starting_vertex)

        # while stack is not empty
        while s.size():
            # pop first item
            v = s.pop()

            # if it hasn't been visited
            if v not in visited:
                # add to visited set
                visited.add(v)

                # print node
                print(f"{v}")

                # add neighbors to stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for next_node in self.get_neighbors(starting_vertex):
                self.dft_recursive(next_node, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # empty queue
        q = Queue()

        # set to store visited nodes
        visited = set()

        # enqueue path to starting vertex
        q.enqueue([starting_vertex])

        # while queue is not empty
        while q.size():
            # dequeue first path
            path = q.dequeue()

            # grab last vertex from path
            v = path[-1]
            # if it hasn't been visited
            if v not in visited:
                if v is destination_vertex:
                    return path
                
                # mark visited
                visited.add(v)

                for next_node in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_node)
                    q.enqueue(new_path)




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # empty stack
        s = Stack()

        # set to store visited nodes
        visited = set()

        # push starting node
        s.push([starting_vertex])

        # while stack is not empty
        while s.size():
            
            # pop first path
            path = s.pop()

            # grab last vertex from path
            v = path[-1]

            # if it hasn't been visited
            if v not in visited:
                if v is destination_vertex:
                    return path

                # add to visited set
                visited.add(v)

                for next_node in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_node)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = self.array_list.pop()

        # pop first path

        if path is None:
            path = [starting_vertex]

        v = path[-1]

        if v not in self.visited:
            if v is destination_vertex:
                return path

            # add to visited set
            self.visited.add(v)

            for next_node in self.get_neighbors(v):
                new_path = path.copy()
                new_path.append(next_node)
                self.array_list.push(new_path)

            return self.dfs_recursive(starting_vertex, destination_vertex)

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
