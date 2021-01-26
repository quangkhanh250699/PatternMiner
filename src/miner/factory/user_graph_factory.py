#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:43:57 2021

@author: quangkhanh
"""

from src.conversation import GraphFactory, Graph, Edge, Node
from src.miner.hasher import GraphHasher
from typing import List


class UserGraphFactory(GraphFactory):
    __map: dict

    def __init__(self, graph_hasher: GraphHasher):
        self.__map = dict()
        self.__graph_hasher = graph_hasher

    def graph(self, nodes: List[Node], edges: List[Edge]) -> Graph:
        
        code = self.__graph_hasher.hash(nodes=nodes, edges=edges)
        if self.contain(code=code):
            return self.__map[code]
        else:
            new_graph = Graph(nodes, edges)
            self.__map[code] = new_graph
            return new_graph

    def contain(self, code=None, nodes=None, edges=None) -> bool:
        _code = None 
        if code is not None: 
            _code = code 
        else: 
            if nodes is not None and edges is not None:
                _code = self.__graph_hasher.hash(edges=edges, nodes=nodes)
            else: 
                raise Exception("input is not right!")
        return _code in self.__map.keys()

    def count(self) -> int:
        return self.__map.__len__()
