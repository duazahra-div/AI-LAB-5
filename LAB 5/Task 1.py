from collections import deque

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def BFS(self, start):
        visited = [False] * self.v
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for i in self.adj[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


g = Graph(5)

g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(4, 3)

print("BFS Traversal:")
g.BFS(0)