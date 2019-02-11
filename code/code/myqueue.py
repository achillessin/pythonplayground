# queue using a list
class MyQueue(object):
	def __init__(self, size):
		self.queue = list()
		self.max_size = size
	def push(self, data):
		if len(self.queue) >= self.max_size:
			raise Exception("Error: max size reached")
		return self.queue.insert(0, data)
	def pop(self):
		return self.queue.pop()
	def peek(self):
		return self.queue[-1]

# queue using a deque
from collections import deque

queue = deque([1,2,3,4],maxlen=10)
queue.append(5)
queue.popleft()
queue.pop()
queue.clear()


# queue with Queue class and threading (producer consumer applicationf
import queue

q = queue.Queue()
q.put(10)
q.put(9)
q.get()

q = queue.PriorityQueue()

class Job:
	def __init__(self, priority):
		self.priority = priority

	def __eq__(self, other):
		return self.priority == other.priority

	def __lt__(self,other):
		return self.priority < other.priority

	def __repr__(self):
		return str(self.priority)
j1 = Job(1)
j2 = Job(2)

q.put(j1)
q.put(j2)

print(q.get())
print(q.get())
