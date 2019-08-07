# Task3_explanation
## Problem description
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.
## Solution
I use binary tree to implement.
![](media/15651059902409/15651075475557.jpg)
Time complexity for while is $O(n)$
Time complexity for sort is $O(nlogn)$
Total Time complexity **Big O equals to** $O(n^2logn)$
Space complexity **Big O equals to**$O(n)$