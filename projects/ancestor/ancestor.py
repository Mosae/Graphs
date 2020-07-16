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
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        #inside the vertices - the key will be the vertex stored in the set
        self.vertices[vertex] = set()

    def add_edges(self, v1, v2):
        self.vetices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]
#Build a path like we did in search
#We dont know when to stop until we've seen everyone
graph = Graph()
def build_graph(ancestors):
    breakpoint()
    #we getting a list of tuples
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        graph.add_vertex(parent)
        graph.add_vertex(child)
        #for everone of the parents, we want to add an edge from parent to child
        graph.add_edges(parent, child)
        


def earliest_ancestor(ancestors, starting_node):
    pass