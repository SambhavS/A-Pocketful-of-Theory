#Lempel–Ziv–Welch Compression Encoder & Decoder (Default set to ASCII, 9-bit))
from string import ascii_letters
from textwrap import wrap
from sys import getsizeof

def LZW_encoder(user_input, d, max_val=255, bit_length=9):
	#Encoding
	nextVal = max_val + 1
	output=[]
	userQ = list(user_input)
	curr=""
	while userQ:
		next_ch = userQ.pop(0)
		if curr + next_ch in d:
			curr += next_ch
		else:
			output.append(d[curr])
			d[curr+next_ch] = nextVal
			curr=next_ch
			nextVal+=1
	output.append(d[curr])

	#Int List -> Binary
	bin_output=""
	for num in output:
		bin_ver = bin(num)[2:] 
		prefixed_zeroes = "0"*(bit_length-len(bin_ver))
		bin_output += prefixed_zeroes + bin_ver
	return int(bin_output,2)

def LZW_decoder(encoded, d, max_val=255, bit_length=9):
	#Binary -> Int List
	encoded_str = str(bin(encoded))[2:]
	stripped_zeroes = "0"*(bit_length-len(encoded_str)%bit_length)
	encoded_str = stripped_zeroes + encoded_str
	encoded = [int(num, 2) for num in wrap(encoded_str, bit_length)]

	#Decoding
	nextVal = max_val + 1
	original=[]
	curr_str = d[encoded.pop(0)]
	original.append(curr_str)
	while encoded:
		next_str = d[encoded.pop(0)]
		original.append(next_str)
		d[nextVal] = curr_str + next_str[0]
		curr_str = next_str
		nextVal += 1
	return ''.join(original)

#Example Usage
initial_dict = {s:ord(s) for s in ascii_letters+" .,!"}
inv_dict = {v: k for k, v in initial_dict.items()}
original = "banana bandana"
encoded = LZW_encoder(original, initial_dict)
decoded = LZW_decoder(encoded, inv_dict)
print()
print("Original:", original)
print("Encoded:", encoded)
print("Decoded:", decoded)
memsaved = round(1000*(getsizeof(encoded)/getsizeof(decoded)))/10
print(str(memsaved)+"%"+" of original ")
print()