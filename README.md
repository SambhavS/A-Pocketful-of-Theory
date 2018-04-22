#  A Pocketful of Theory

Here's a small bunch of some of more conventional programs I'm writing. Most of these will be implementations of data structures or algorithms, but I might throw in a few attempts to solve interesting problems my friends tell me.


**Knapsack Problem |**
The knapsack problem has three main variations: unbounded, 1/0 (most common), and bounded (hardest). I implemented DP solutions for both the unbounded and 1/0 variations. 


**Huffman Encoding |**
I implemented a huffman encoder that takes in a string and comes up with a Huffman tree which it uses to create a compressed binary of the given string.


**Short Sorts |**
In APCS, I was taught that QuickSort and MergeSort take a lot of code to implement, particularly in Java. 
Here they are implemented in just a few lines of python.


**ManyWordsProblem |**
A friend told me this problem and I call it the many words problem.


It goes like this: Given a set of words and a string containing many words concatenated together without spaces,
write a function that determines whether the given string is made entirely of words from the dictionary.


For example f( "hellohowdyhi" , {"hello","howdy","hi"} ) should return True and f( "hellohellohello" , {"hello","hi"} ) should also return True. However f( "hotdog" , {"ho","ot","dog"} ) should return False.

I thought it would be fun to find a one-line solution which I implemented here. The actually good solution also implements memoization.
