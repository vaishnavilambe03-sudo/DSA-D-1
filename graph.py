# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex,":", self.adjacency_list[vertex])

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             self.adjacency_list[vertex1].append(vertex2)
#             return True
#         return False
    
#     def remove_vertex(self, vertex):
#         if vertex in self.adjacency_list:

#             for other_vertex in self.adjacency_list:
#                 if vertex in self.adjacency_list[other_vertex]:
#                     self.adjacency_list[other_vertex].remove(vertex)

#             del self.adjacency_list[vertex]
#             return True
#         return False
        
# my_graph = Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")
# my_graph.add_edge("A","B")
# my_graph.add_edge("A","C")
# my_graph.add_edge("A","D")
# my_graph.add_edge("B","A")
# my_graph.add_edge("B","E")
# my_graph.add_edge("C","A")
# my_graph.add_edge("C","D")
# my_graph.add_edge("D","A")
# my_graph.add_edge("D","C")
# my_graph.add_edge("D","E")
# my_graph.add_edge("E","B")
# my_graph.add_edge("E","D")
# print("Before Removing:")
# my_graph.print_graph()
# my_graph.remove_vertex("E")
# print("\nAfter Removing E:")
# my_graph.print_graph()

# class Graph:
#     def __init__(self,vertices):
#         # Total number of vertices
#         self.V = vertices

#         # create adjancency matrix with all 0s
#         self.matrix =[[0 for _ in range(vertices)]
#                    for _ in range(vertices)]   

#     def display(self):
#         for row in self.matrix:
#             print(row)
# g = Graph(4)
# print("adjancy matrix",g)
# g.display()

#Hashing is a technique used to convert data into a fixed size value or hash code.

# class Graph:
#     def __init__(self,vertices):
#         # Total number of vertices
#         self.V = vertices

#         # create adjancency matrix with all 0s
#         self.matrix =[[0 for _ in range(vertices)]
#                    for _ in range(vertices)] 

#     def add_edge(self,u,v):
#             self.matrix[u][v]=1
#             self.matrix[v][u]=1   #For undirected graph 

#     def remove_edge(self,u,v):
#          self.matrix[u][v]=0
#          self.matrix[v][u]=0      

#     def display(self):
#         for row in self.matrix:
#             print(row)
# g = Graph(4)
# # Add egdes
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)
# print("adjancy matrix",g)
# g.display()

class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)


h = HashTable(10)

h.insert(15)
h.insert(25)
h.insert(35)
h.display()