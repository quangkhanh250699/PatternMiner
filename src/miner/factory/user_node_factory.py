#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:43:11 2021

@author: quangkhanh
"""

from src.conversation import Node, NodeFactory


class UserNodeFactory(NodeFactory): 
    
    __map: dict
    
    def __init__(self):
        self.__map = dict()
    
    def node(self, name: str) -> Node:
        if name in self.__map.keys():
            return self.__map[name]
        else: 
            new_node = Node(name)
            self.__map[name] = new_node
            return new_node

    def contain(self, code: str) -> bool:
        return code in self.__map.keys()

    def count(self) -> int:
        return self.__map.__len__()
