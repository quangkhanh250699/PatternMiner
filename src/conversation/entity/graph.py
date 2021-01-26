#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:59:58 2021

@author: quangkhanh
"""

from src.conversation.entity.node import Node
from src.conversation.entity.edge import Edge

from typing import Set

class Graph: 
    
    __nodes: Set[Node]
    __edges: Set[Edge]
    
    
    def __init__(self, nodes, edges): 
        self.__nodes = set(nodes)
        self.__edges = set(edges)
        
    @property 
    def nodes(self):
        return self.__nodes 
    
    @property 
    def edges(self): 
        return self.__edges 
