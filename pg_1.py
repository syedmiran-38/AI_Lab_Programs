# Write a python program to implement DFS transversal

class Graph:
    def __init__(self):
        self.graph = {}


    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]


    def dfs(self, start):
        visited = set()
        self.dfs_helper(start, visited)


    def dfs_helper(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        if node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self.dfs_helper(neighbor, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')


    print("DFS traversal starting from node 'A':")
    g.dfs('A')