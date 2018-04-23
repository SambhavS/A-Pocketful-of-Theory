#Huffman Compression Coding (Encoder & Decoder)
from heapq import *
from sys import getsizeof

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

def huffman_encoder(user_input):
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
		return int(''.join([binDict[eachchar] for eachchar in user_input]),2), huffF

def huffman_decoder(user_input, hufftree):
	decoded = ""
	user_str = [i for i in bin(user_input)[2:]]
	curr_node = hufftree
	while user_str:
		if curr_node.val:
			decoded += curr_node.val
			curr_node = hufftree
		else:
			next_bit = int(user_str.pop(0))
			if next_bit == 0:
				curr_node = curr_node.left
			if next_bit == 1:
				curr_node = curr_node.right
	if curr_node.val:
		decoded += curr_node.val
	return decoded

def printSummary(encoded, decoded, original):
	print()
	print("Original:", original)
	print("Encoded:", encoded)
	print("Decoded:", decoded)
	memsaved = round(1000*(getsizeof(encoded)/getsizeof(original)))/10
	print(str(memsaved)+"%"+" of original ")
	print()
	

#Example Usage
original = "happy hungry hippo"
encoded, hufftree = huffman_encoder(original)
decoded = huffman_decoder(encoded, hufftree)
printSummary(encoded, decoded, original)