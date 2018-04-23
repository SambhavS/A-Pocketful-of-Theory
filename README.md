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
For Huffman Coding & LZW Coding, I implemented an encoder and decoder for each. 


For the Knapsack problem, I implemented a solution to the unbounded and 1/0 variations of the problem. 


For Bellman-Ford, I implemented the algorithm simply using tuples to represent edges and a list of chars to represent node labels. 


For Short Megesort/Quicksort, I wrote some ugly but very short code to implement them, for fun, mostly because APCS gave us the impression that they take long masses of Java to implement. 


For ManyWordsProblem, I wrote a pretty ugly one-liner that solves it (actually good solution should also implement memoization). The problem goes like this:
> Given a set of words and a string containing many words concatenated together without spaces,
> write a function that determines whether the given string is made entirely of words from the dictionary.
>
> For example f( "hellohowdyhi" , {"hello","howdy","hi"} ) should return True and f( "hellohellohello" , {"hello","hi"} ) 
> should also return True. However f( "hotdog" , {"ho","ot","dog"} ) should return False.
