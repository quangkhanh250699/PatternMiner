#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:04:38 2021

@author: quangkhanh
"""

from src.miner.hasher.hasher_base import Hasher


class EdgeHasher(Hasher):

    def __init__(self, node_hasher):
        self.__node_hasher = node_hasher

    def hash(self, edge=None, node_from=None, node_to=None):
        node1 = None
        node2 = None
        if edge is not None:
            node1 = edge.node_from
            node2 = edge.node_to
        else:
            if node_from is not None and node_to is not None:
                node1 = node_from
                node2 = node_to
            else:
                raise Exception("input is not right!")
        return self.__node_hasher.hash(node1) + "->" \
               + self.__node_hasher.hash(node2)
