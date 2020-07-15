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
            self.vertices[v1].add(v2) #theres an edge from v1 to v2
        else:
            raise IndexError('Vert does not exist')

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
        #create an empty queue
        still_to_visit = Queue()
        # A SET TO SORE THE VISITED NODES
        visited = set()
        #init: enqueue the starting node
        still_to_visit.enqueue(starting_vertex)
        #While queue is not empty
        while still_to_visit.size() > 0:
            #Dequeue the first item
            curr_path_to_last_vertex = still_to_visit.dequeue()
            #if it'still_to_visit not been visited:
            if curr_path_to_last_vertex not in visited:
                #Mark as visited - Add to visited set
                #print it out
                print(curr_path_to_last_vertex)
                visited.add(curr_path_to_last_vertex)

                #print(f'Q: breadth first search - Visited {curr_path_to_last_vertex}')
                # add all neighbours(unvisited) to the queue
                for neighbor in self.get_neighbors(curr_path_to_last_vertex):
                    still_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         #create an empty queue
        still_to_visit = Stack()
        # A SET TO SORE THE VISITED NODES
        visited = set()
        #init: enqueue the starting node
        still_to_visit.push(starting_vertex)
        #While queue is not empty
        while still_to_visit.size() > 0:
            #Dequeue the first item
            curr_path_to_last_vertex = still_to_visit.pop()
            #if it'still_to_visit not been visited:
            if curr_path_to_last_vertex not in visited:
                #Mark as visited - Add to visited set
                print(curr_path_to_last_vertex)
                visited.add(curr_path_to_last_vertex)

                # add all neighbours to the queue
                for neighbor in self.get_neighbors(curr_path_to_last_vertex):
                    if neighbor not in visited:

                        still_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex,visited_vertices=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if visited vertices is none
        if visited_vertices is None:
            # if visited vertices is none change to a set
            visited_vertices = set()
        # add starting vertex to visited vertices
        visited_vertices.add(starting_vertex)
        # print current starting vertex
        print(starting_vertex)
        # get the neighbors from the starting vertex
        neighbors = self.get_neighbors(starting_vertex)
        # check if there are neighbors in the neighbors var
        while len(neighbors) > 0:
            # for each of the neighbors
            for neighbor in neighbors:
                #print(f"this is the neighbors", {neighbor})
                # if the neighbor is not in the visited vertices
                if neighbor not in visited_vertices:
                    # run the dft_recur function again
                    # this time with neighbor as the starting vertex, and visited_vertices as the visites
                    self.dft_recursive(neighbor, visited_vertices)
                else:
                    return


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest current_path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue 
        bft_path = Queue()
        # and enqueue A PATH TO the starting vertex ID
        #still_to_visit.enqueue([starting_vertex])
        bft_path.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while bft_path.size() > 0:
            # Dequeue the first PATH
            current_path = bft_path.dequeue()
            # Grab the last vertex from the PATH
            curr_path_to_last_vertex = current_path[-1]
            # If that path to vertex has not been visited...
            if curr_path_to_last_vertex not in visited:   
                # CHECK IF IT'S THE TARGET
                if curr_path_to_last_vertex == destination_vertex:
                  # IF SO, RETURN PATH
                    return current_path
                # Mark it as visited...
                else:
                    visited.add(curr_path_to_last_vertex)
                    neighbors = self.get_neighbors(curr_path_to_last_vertex)
                # copy path and add neighbour to them
                    for neighbor in neighbors:
                        #copy path
                        copy_curr_path = current_path[:]
                        #lets add the neighbour
                        copy_curr_path.append(neighbor)
                        #add the new path - copy
                        bft_path.enqueue(copy_curr_path)    
                
  
 

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a current_path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #empty stack
        dfs_path = Stack()
        #add path to starting vertex
        dfs_path.push([starting_vertex])
        #print(starting_vertex)
        #create a set for visited vetices
        visited_vertices = set()
        #while path is not empty
        while dfs_path.size() > 0:
            #pop first path
            current_path = dfs_path.pop()
            #last vertex in path
            curr_path_to_last_vertex = current_path[-1]
            #if we have not made it there yet
            if curr_path_to_last_vertex not in visited_vertices:
                #print(curr_path_to_last_vertex)
                #see if current is the destination
                if curr_path_to_last_vertex == destination_vertex:
                    #if true we found our destination - return
                    return current_path
                #if not - we mark as visited 
                else:
                    #fetch the neighbour and make copy of the path there
                    visited_vertices.add(curr_path_to_last_vertex)
                    neighbors = self.get_neighbors(curr_path_to_last_vertex)
                    for neighbor in neighbors:
                        #print(f'Neighbour', {neighbor})
                        #duplicate the path
                        current_path_copy = current_path[:]
                        #add the neighbour
                        current_path_copy.append(neighbor)
                        #we add new path 
                        dfs_path.push(current_path_copy)
                           
        
    def dfs_recursive(self, starting_vertex, destination_vertex, dfs_path=Stack(), visited=None):
        """
        Return a list containing a current_path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #create empty set for visited and path
        
        visited = set()
        #path to begin search
        curr_path = dfs_path.pop()
        #if curr path is none - at the start
        if curr_path == None:
            #include current path to the starting vertex
            curr_path = [starting_vertex]
        #check to see if last vert in the Stack is not in visited
        if curr_path[-1] not in visited:
            #add that last item to the visited
            visited.add(curr_path[-1])
            #get last items neighbor
            for neighbor in self.get_neighbors(curr_path[-1]):
                #if neighbor is the destination, we found what we looking for
                if neighbor == destination_vertex:
                    #append neighbor to path
                    curr_path.append(neighbor)
                    #return path
                    return curr_path
                #Make a copy of the curr path to make a new path
                current_copy_of_path = curr_path.copy()
                #add neighbor to new path
                current_copy_of_path.append(neighbor)
                #push new path to main path
                dfs_path.push(current_copy_of_path)
            #if we get here - call the function again 
            return self.dfs_recursive(starting_vertex, destination_vertex, dfs_path, visited)
                


        

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
    Valid BFS current_path:
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
