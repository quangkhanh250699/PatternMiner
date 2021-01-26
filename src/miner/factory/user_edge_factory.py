#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:43:43 2021

@author: quangkhanh
"""

from src.conversation import Edge, EdgeFactory, Node
from src.miner.hasher import EdgeHasher


class UserEdgeFactory(EdgeFactory):

    __map: dict

    def __init__(self, edge_hasher: EdgeHasher):
        self.__map = dict()
        self.__edge_hasher = edge_hasher

    def edge(self, node_from: Node, node_to: Node) -> Edge:
        code = self.__edge_hasher.hash(node_from=node_from, node_to=node_to)
        if self.contain(code):
            return self.__map[code]
        else:
            new_edge = Edge(node_from, node_to)
            self.__map[code] = new_edge
            return new_edge

    def contain(self, code: str) -> bool:
        return code in self.__map.keys()

    def count(self) -> int:
        return self.__map.__len__()
