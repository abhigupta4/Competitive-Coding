#Output q lines, each line containing the maximum possible weight of the match for given query, else -1, in case no valid result is obtained.

class TrieNode():
	def __init__(self):
		self.children = [None]*26
		self.max1 = 0


class Trie():
	def __init__(self):
		self.head = TrieNode()

	def insert(self, string1, value):
		cur = self.head
		for ele in string1:
			posi = ord(ele)-ord('a')

			if cur.children[posi] == None:
				cur.children[posi] = TrieNode()
				cur.children[posi].max1 = value
			else:
				cur.children[posi].max1 = max(cur.children[posi].max1, value)

			cur = cur.children[posi]

	def query(self, pattern):
		cur = self.head
		for ele in pattern:
			posi = ord(ele)-ord('a')

			if cur.children[posi] == None:
				return -1
			else:
				cur = cur.children[posi]

		return cur.max1


n,q = map(int, raw_input().split())

main1 = Trie()

for _ in xrange(n):
	a,b = raw_input().split()
	main1.insert(a, int(b))

for _ in xrange(q):
	pat1 = raw_input()
	print main1.query(pat1)