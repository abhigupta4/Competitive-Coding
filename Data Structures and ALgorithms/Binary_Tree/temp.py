class Node:
	def __init__(self,data):
		self.val = data
		self.left = None
		self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
print root
