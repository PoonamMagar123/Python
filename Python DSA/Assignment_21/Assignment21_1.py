class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, source, dest, weight=1):
        self.adj_matrix[source][dest] = weight
        if self.is_undirected_graph():
            self.adj_matrix[dest][source] = weight

    def remove_edge(self, source, dest):
        self.adj_matrix[source][dest] = 0
        if self.is_undirected_graph():
            self.adj_matrix[dest][source] = 0

    def has_edge(self, source, dest):
        return self.adj_matrix[source][dest] != 0

    def is_undirected_graph(self):
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.adj_matrix[i][j] != self.adj_matrix[j][i]:
                    return False
        return True

    def print_adj_matrix(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(f"{self.adj_matrix[i][j]:3d}", end=" ")
            print()

# Create a graph with 5 vertices
graph = Graph(5)

# Add edges
graph.add_edge(0, 1)
graph.add_edge(1, 2, weight=2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Check if there is an edge between vertex 1 and 2
if graph.has_edge(1, 2):
    print("Edge exists between vertex 1 and 2")

# Print the adjacency matrix
graph.print_adj_matrix()

