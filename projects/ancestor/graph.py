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
        if v1 not in self.vertices:
            self.add_vertex(v1)
        self.vertices[v1].add(v2)
        # if v1 in self.vertices and v2 in self.vertices:
        #     self.vertices[v1].add(v2)   # there's an edge from v1 to v2
        # else:
        #     raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        return None
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            value = queue.dequeue()
            if value not in visited:
                visited.add(value)
                # print(value)
                if self.get_neighbors(value) is not None:
                    for neighbor in self.get_neighbors(value):
                        queue.enqueue(neighbor)
                else:
                    continue

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)

        while stack.size() > 0:
            value = stack.pop()
            if value not in visited:
                visited.add(value)
                print(value)
                for neighbor in self.get_neighbors(value):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_inside(stack, visited = set()):
            if stack.size() <= 0:
                return
            value = stack.pop()
            if value not in visited:
                visited.add(value)
                print(value)
                for nieghbor in self.get_neighbors(value):
                    stack.push(nieghbor)
                dft_inside(stack, visited)
        stack = Stack()
        stack.push(starting_vertex)
        dft_inside(stack)
        


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            # print("this is queue",queue.queue )
            path = queue.dequeue()
            value = path[-1]
            if value not in visited:
                if value == destination_vertex:
                    return path
                visited.add(value)
                for neighbor in self.get_neighbors(value):
                    newPath = list(path)
                    newPath.append(neighbor)
                    queue.enqueue(newPath)

            

    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        while stack.size() > 0:
            # print("this is stack",stack.stack )
            path = stack.pop()
            value = path[-1]
            if value not in visited:
                if value == destination_vertex:
                    return path
                visited.add(value)
                for neighbor in self.get_neighbors(value):
                    newPath = list(path)
                    newPath.append(neighbor)
                    stack.push(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        shortPath = []
        def dfs_inside(stack,visited = set()):
            path = stack.pop()
            value = path[-1]
            if value == destination_vertex:
                shortPath.append(path)
                return path
            elif value not in visited:
                visited.add(value)
                for neighbor in self.get_neighbors(value):
                    newPath = list(path)
                    newPath.append(neighbor)
                    stack.push(newPath)
                    dfs_inside(stack)
        stack = Stack()
        stack.push([starting_vertex])
        dfs_inside(stack)
        return shortPath[0]
        


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
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
     '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
