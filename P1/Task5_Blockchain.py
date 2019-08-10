#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/8/6 9:56 AM 
# @Author : Yuchen 
# @File : Task5_Blockchain.py 
# @Software: PyCharm

import hashlib
import time


class Block:

    def __init__(self, data, previous_hash=None):
        self.timestamp = self.get_utc_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        print("timestamp:{}, hash:{}".format(self.timestamp, self.hash))
        self.next = None

    def get_utc_time(self):
        timestamp = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
        return timestamp

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
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

        previous_hash = current_block.hash
        block.previous_hash = previous_hash
        current_block.next = block


if __name__ == '__main__':
    block1 = Block("hello")
    block2 = Block("how")
    block3 = Block("are")
    block4 = Block("U")

    BlockChain = BlockChain()
    BlockChain.add_block(block1)
    BlockChain.add_block(block2)
    BlockChain.add_block(block3)
    BlockChain.add_block(block4)
    # Test1, edge test
    print(BlockChain.block_head.previous_hash)

    # Test2, hash of block2, should return "ba78973ddcf98d4e5369f5e722d681d94f5106895e5d6cf6fa3ca8240fabdc14"
    print(BlockChain.block_head.next.next.hash)

    # Test3, previous hash of block3, should return "ba78973ddcf98d4e5369f5e722d681d94f5106895e5d6cf6fa3ca8240fabdc14"
    print(BlockChain.block_head.next.next.next.previous_hash)
