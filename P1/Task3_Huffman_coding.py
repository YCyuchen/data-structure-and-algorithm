#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/6 10:42 PM 
# @Author : Yuchen 
# @File : Task3_Huffman_coding.py 
# @Software: PyCharm
import sys


def char_frequency(data):
    frequency = {}
    for character in data:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency


def assign_code(nodes, label, result, prefix=''):
    childs = nodes[label]
    tree = {}
    if len(childs) == 2:
        tree['0'] = assign_code(nodes, childs[0], result, prefix + '0')
        tree['1'] = assign_code(nodes, childs[1], result, prefix + '1')
        return tree
    else:
        result[label] = prefix
        return label


def huffman_encoding(data):
    frequency = char_frequency(data)
    vals = frequency.copy()
    nodes = {}

    # edge case: input data is empty
    if len(frequency) == 0:
        print("Error: input is empty")
        return "", {}
    # edge case: input only have same char
    if len(frequency) == 1:
        encode_data = ''.join('0' for _ in data)
        tree = {'0': data[0]}
        return encode_data, tree

    # leafs initialization
    # initialized node should look like  nodes = {'T': [], 'h': [], 'e': [], ' ': [], 'b': [], ...}
    for n in vals.keys():
        nodes[n] = []
    while len(vals) > 1:  # binary tree creation
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1 + a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1 + a2] = [a1, a2]
    code = {}
    root = a1 + a2
    tree = assign_code(nodes, root, code)  # assignment of the code for the given binary tree
    print("node\n", nodes)
    encode_data = ''.join(code[i] for i in data)
    return encode_data, tree


def huffman_decoding(data, tree):
    decoded = []
    i = 0
    while i < len(data):  # decoding using the binary graph
        ch = data[i]
        act = tree[ch]
        while not isinstance(act, str):
            i += 1
            ch = data[i]
            act = act[ch]
        decoded.append(act)
        i += 1

    return ''.join(decoded)


if __name__ == "__main__":
    # Test 1
    print("--------------------Test case1 -------------------------")
    # a_great_sentence = "The bird is the word"
    a_great_sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test 2, edge test
    print("--------------------Test case2 -------------------------")
    a_great_sentence = "aaaaa"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test 3, edge test
    print("--------------------Test case3 -------------------------")
    a_great_sentence = ""
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
