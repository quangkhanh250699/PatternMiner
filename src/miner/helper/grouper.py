#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:35:24 2021

@author: quangkhanh
"""

from src.miner.helper.comparator import Comparator


class Grouper:
    
    def __init__(self, comparator: Comparator):
        self.__comparator = comparator 
        
    def group(self, elements: list):
        layers = [] 
        size = len(elements)
        pool = elements.copy()
        while len(pool) > 0:
            layer = []
            length = len(pool)
            for i in range(length):
                is_dominated = False
                for j in range(length):
                    if self.__comparator.compare(pool[j], pool[i]):
                        is_dominated = True
                        break 
                if not is_dominated:
                    layer.append(pool[i])
            for element in layer: 
                pool.remove(element)
            layers.append(layer)
        return layers
