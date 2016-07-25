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

	
for _ in xrange(input()):
	ds = Disjoint_Set()
	P = input()
	N = input()
	# for i in xrange(N):
	# 	ds.make_set(i+1)
	M = input()
	li = []
	for m in xrange(M):
		u,v,c = map(int,raw_input().split())
		ds.make_set(u)
		ds.make_set(v)
		li.append([c,u,v])
	li.sort()
	cost = 0
	for c,u,v in li:
		if ds.find_set1(u) != ds.find_set1(v):
			ds.union(u,v)
			cost += c
			# print cost
	print cost*P