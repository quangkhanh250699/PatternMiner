#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:30:22 2021

@author: quangkhanh
"""

from src.conversation import Graph, Edge, Node, Flow, \
    GraphFactory, EdgeFactory, NodeFactory
    
    
class GraphExtractor:
    
    def __init__(self, graph_factory: GraphFactory,
                 edge_factory: EdgeFactory,
                 node_factory: NodeFactory):
        self.__graph_factory = graph_factory
        self.__edge_factory = edge_factory 
        self.__node_factory = node_factory
        
    def extract(self, flow: Flow) -> Graph: 
        nodes = self._to_nodes(flow)
        edges = self._to_edges(flow)
        graph = self.__graph_factory.graph(nodes, edges)
        return graph
        
    def _to_nodes(self, flow: Flow):
        return [self.__node_factory.node(name) for name in flow.flow]
    
    def _to_edges(self, flow: Flow):
        nodes = self._to_nodes(flow)
        size = nodes.__len__()
        edges = []
        for i in range(0, size-1):
            edge = self.__edge_factory.edge(nodes[i], nodes[i+1])
            edges.append(edge)
        return edges
    