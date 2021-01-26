#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:23:21 2021

@author: quangkhanh
"""

from src.miner.hasher.hasher_base import Hasher 
from src.conversation import Node

class NodeHasher(Hasher):
    
    def hash(self, node: Node) -> str: 
        return node.name