from util import Stack
#UPPER
#Understood: given the number, look up to find the last node connected to that tree. If it has no 
#neigbor - return -1
#this is a longest path problem

#Plan
## Graphs problem solving
## translate the problem
## Nodes: People
## Edges: When a child has a parent

## Build graph or define get neighbors

## Choose algorithm 
# Either algo(BFS or DFS) will work
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        #inside the vertices - the key will be the vertex stored in the set
        if vertex not in self.vertices:
           self.vertices[vertex] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')    

    #get all neighbor edges of vertex
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

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

def earliest_ancestor(ancestors, starting_node):
    #create graph
    ancestor_graph = Graph()
    #make a path
    paths = []

    #add vertices to graph
    for vertex in range(0,20):
        ancestor_graph.add_vertex(vertex)
    #add edges to graph
    for ancestor in ancestors:
        ancestor_graph.add_edges(ancestor[0], ancestor[1])
    #add path to ancestor path
    for vertex in ancestor_graph.vertices:
        if ancestor_graph.dfs(vertex,starting_node) is not None and len(ancestor_graph.dfs(vertex, starting_node)) > 0:
            paths.append(ancestor_graph.dfs(vertex, starting_node))

    if len(paths) == 1:
        return -1
    #find earliest neighbor
    begin_path = paths[0]
    for path in paths:
        if len(path) > len(begin_path) or len(begin_path) and path[0] < begin_path[0]:
            begin_path = path

    return begin_path[0]                             