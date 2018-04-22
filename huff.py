from heapq import *
class Node:
	def __init__(self, num, val=None, left=None, right=None):
		self.num, self.val, self.left, self.right = num, val, left, right
	def __lt__(self, other):
		return self.num < other.num
	def addcode(self, code):
		self.code = code
		if(self.left and self.right):
			self.left.addcode(code+"0")
			self.right.addcode(code+"1")
	def binMap(self, binD):
		binD[self.val] = self.code
		if(self.left and self.right):
			self.left.binMap(binD)
			self.right.binMap(binD)
def huffman(user_input):
	charCount, h = {}, []
	for char in user_input:
		if char not in charCount:
			charCount[char] = 0
		charCount[char] += 1
	freq_list = [Node(num=freq, val=value) for value, freq in list(charCount.items())]
	[heappush(h, node) for node in freq_list]
	try:
		while(True):
			small1 = heappop(h)
			small2 = heappop(h)
			sub_tree = Node(num=small1.num + small2.num, left=small1, right=small2)
			heappush(h, sub_tree)
	except IndexError:
		huffF = small1
		huffF.addcode("")
		binDict={}
		huffF.binMap(binDict)
		return ''.join([binDict[eachchar] for eachchar in user_input])
#Example Usage
print(huffman("happy hungry hippo"))
