#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:56:27 2021

@author: quangkhanh
"""

from src.conversation import Graph, Edge, Node 

class GraphComparator:
    
    def __init__(self):
        pass 
    
    def compare(self, graph1: Graph, graph2: Graph) -> bool:
        '''
        Compare graph1 with graph2

        Parameters
        ----------
        graph1 : Graph
            based graph.
        graph2 : Graph
            compared graph.

        Returns
        -------
        bool
            True if graph1 dominates graph2.
            Else False.
        '''
        edges1 = graph1.edges
        edges2 = graph2.edges 
        nodes1 = graph1.nodes
        nodes2 = graph2.nodes 
        
        if nodes2.issubset(nodes1):
            if edges2.issubset(edges1):
                if nodes1.__len__() > nodes2.__len__() or \
                    edges1.__len__() > edges2.__len__():
                        return True
        return False
        