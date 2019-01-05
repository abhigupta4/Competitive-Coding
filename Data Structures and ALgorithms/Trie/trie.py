class trienode:
	def __init__(self,end=0):
		self.map1 = {}
		self.end = end


class Trie():
	def __init__(self):
		self.map1 = {}
		self.end = 0
	def insert(word):
		cur = self
		for letter in word:
			if letter not in cur.map1:
				cur.map1[letter] = trienode()
			cur  = cur[letter]
		cur.end = 1