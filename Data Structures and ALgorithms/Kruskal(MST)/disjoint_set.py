#O(m) where m is number of operations
class Node:
	def __init__(self,data):
		self.data = data
		self.parent = 0
		self.rank = 0

class Disjoint_Set:
	def __init__(self):
		self.di = {}

	def make_set(self,data):
		node = Node(data)
		node.parent = node
		node.rank = 0
		self.di[data] = node

	def find_set1(self,val):
		return self.find_set(self.di[val]).data

	def find_set(self,node):
		# print "hi"
		parent = node.parent
		if(parent == node):
			return parent
		node.parent = self.find_set(node.parent)
		return node.parent

	def union(self,data1,data2):
		node1 = self.di[data1]
		node2 = self.di[data2]
		parent1 = self.find_set(node1)
		parent2 = self.find_set(node2)
		if(parent1.data == parent2.data):
			return
		if(parent1.rank > parent2.rank):
			parent2.parent = parent1
		elif (parent1.rank == parent2.rank):
			parent1.rank += 1
			parent2.parent = parent1
		else:
			parent1.parent = parent2

	

ds = Disjoint_Set()
for i in xrange(1,8):
	ds.make_set(i)

ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)
for i in xrange(1,8):
	print ds.find_set1(i)
