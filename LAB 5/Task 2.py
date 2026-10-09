from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = []

        self.adj[v].append(w)

        if w not in self.adj:
            self.adj[w] = []

    def BFS(self, start, goal):
        visited = [start]
        queue = deque([start])

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node == goal:
                print("\nGoal Found!")
                return True

            for i in self.adj[node]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        print("\nGoal not Found")
        return False           


g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'F')
g.addEdge('A', 'D')
g.addEdge('A', 'E')

g.addEdge('B', 'K')
g.addEdge('B', 'J')

g.addEdge('D', 'G')

g.addEdge('E', 'C')
g.addEdge('E', 'H')
g.addEdge('E', 'I')

g.addEdge('K', 'N')
g.addEdge('K', 'M')

g.addEdge('I', 'L')

print("BFS Traversal:")
g.BFS('A', 'G')

ch = input("Enter goal: ")
g.BFS('A', ch)