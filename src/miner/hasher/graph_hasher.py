#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:23:31 2021

@author: quangkhanh
"""

from src.miner.hasher.edge_hasher import EdgeHasher
from src.miner.hasher.node_hasher import NodeHasher
from src.miner.hasher.hasher_base import Hasher 


class GraphHasher(Hasher):
    
    __map: dict
    
    def __init__(self, node_hasher: NodeHasher, edge_hasher: EdgeHasher): 
        self.__node_hasher = node_hasher 
        self.__edge_hasher = edge_hasher 
    
    def hash(self, graph=None, edges=None, nodes=None):
        _edges = None
        _nodes = None
        
        if graph != None:
            _edges = graph.edges
            _nodes = graph.nodes
        else: 
            if edges != None and nodes != None: 
                _edges = edges 
                _nodes = nodes 
            else: 
                raise Exception("input is not right!")
        return self.__hash(set(_nodes), set(_edges))
        
    def __hash(self, nodes, edges) -> str:
        node_codes = [self.__node_hasher.hash(node) for node in nodes]
        edge_codes = [self.__edge_hasher.hash(edge) for edge in edges]
        node_codes.sort()
        edge_codes.sort()
        edges_str = "&".join(edge_codes)
        nodes_str = "&".join(node_codes)
        return nodes_str + "!!!" + edges_str
