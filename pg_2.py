# Write a python program to implement BFS transversal

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def bfs(self, start):
        visited = set()
        queue = deque()
        visited.add(start)
        queue.append(start)

        while queue:
            node = queue.popleft()
            print(node, end=' ')

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')

    print("BFS traversal starting from node 'A':")
    g.bfs('A')
