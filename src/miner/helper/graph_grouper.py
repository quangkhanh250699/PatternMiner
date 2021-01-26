#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:01:53 2021

@author: quangkhanh
"""

from src.conversation import Graph
from src.miner.helper.graph_comparator import GraphComparator

from typing import List

class GraphGrouper():
    
    def __init__(self, compator=GraphComparator()):
        self.__graph_comparator = compator
    
    
    def group(self, graphs: List[Graph]) -> List[List[Graph]]:
        result = []
        while(graphs.__len__() > 0):
            current_layer = []
            for graph in graphs: 
                is_dominated = False
                for opponent in graphs: 
                    if self.__graph_comparator.compare(opponent, graph):
                        is_dominated = True
                if not is_dominated:
                    current_layer.append(graph)
            for graph in current_layer: 
                graphs.remove(graph)
            print("Done layer {}".format(len(result)))
            result.append(current_layer)
        return result
            
    
    