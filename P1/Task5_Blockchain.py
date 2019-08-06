#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/6 9:56 AM 
# @Author : Yuchen 
# @File : Task5_Blockchain.py 
# @Software: PyCharm

import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        print(self.hash)
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.block_head = None

    def add_block(self, block):
        if self.block_head is None:
            self.block_head = block
            return

        current_block = self.block_head
        while current_block.next:
            current_block = current_block.next
        current_block.next = block


if __name__ == '__main__':
    block1 = Block("10:10", "2019", "")
    block2 = Block("10:20", "2019", block1.hash)
    block3 = Block("10:20", "2019", block2.hash)

    BlockChain = BlockChain()
    BlockChain.add_block(block1)
    BlockChain.add_block(block2)
    BlockChain.add_block(block3)
