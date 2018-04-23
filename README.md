#  A Pocketful of Theory

Here's a small bunch of some of more conventional programs I'm writing. Most of these will be implementations of data structures or algorithms, but I might throw in a few attempts to solve interesting problems my friends tell me.


Topics include:
* Bellman-Ford Algorithm
* Knapsack Problem
* Huffman Coding
* Lempel-Ziv-Welch (LZW) Coding
* Short MergeSort/QuickSort
* Many Words Problem

## Some Notes
For Huffman Coding & LZW Coding, I implemented an encoder and decoder for each. For the Knapsack problem, I implemented a solution to the unbounded and 1/0 variations of the problem. For Bellman-Ford, I implemented the algorithm simply using tuples to represent edges and a list of chars to represent node labels.


**Short Sorts |**
In APCS, I was taught that QuickSort and MergeSort take a lot of code to implement, particularly in Java. 
I wrote some ugly but very short solutions, for fun.

**ManyWordsProblem |**
A friend told me this problem and I call it the many words problem.


It goes like this: Given a set of words and a string containing many words concatenated together without spaces,
write a function that determines whether the given string is made entirely of words from the dictionary.


For example f( "hellohowdyhi" , {"hello","howdy","hi"} ) should return True and f( "hellohellohello" , {"hello","hi"} ) should also return True. However f( "hotdog" , {"ho","ot","dog"} ) should return False.

I wrote a an ugly one-liner to solve it, for fun.
