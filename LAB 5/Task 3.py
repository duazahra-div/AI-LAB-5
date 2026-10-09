#PRIORITY QUEUE 
import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def addTask(self, priority, task):
        heapq.heappush(self.pq, (priority, task))

    def showTasks(self):
        print("Priority Queue Order:")

        while self.pq:
            priority, task = heapq.heappop(self.pq)
            print(task)


pq = PriorityQueue()

pq.addTask(3, "Task C")
pq.addTask(1, "Task A")
pq.addTask(2, "Task B")


pq.showTasks()