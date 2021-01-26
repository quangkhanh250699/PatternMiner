#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:48:53 2021

@author: quangkhanh
"""

from src.conversation import Graph, Node, Edge, GraphFactory


class GraphOperator: 
    
    def __init__(self, graph_factory: GraphFactory): 
        self.__graph_factory = graph_factory
        
    def subtract(self, graph1: Graph, graph2: Graph):
        nodes1 = graph1.nodes
        edges1 = graph1.edges
        nodes2 = graph2.nodes 
        edges2 = graph2.edges 
        
        new_nodes = nodes1 - nodes2 
        new_edges = edges1 - edges2 
        
        return self.__graph_factory.graph(new_nodes, new_edges)
        