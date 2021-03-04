#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:43:20 2021

@author: quangkhanh
"""

from typing import List 

from src.miner.extractor.flow_extractor import FlowExtractor
from src.miner.extractor.graph_frequent_extractor import GraphFrequencyExtractor
from src.miner.extractor.graph_extractor import GraphExtractor
from src.conversation import GraphFactory
from src.conversation import Graph, Flow
from src.miner.hasher import GraphHasher
from src.miner.helper import GraphGrouper, GraphOperator, GraphComparator

class UniqueFrequentExtractor():
    
    def __init__(self,
                 flow_extractor: FlowExtractor,
                 graph_hasher: GraphHasher, 
                 graph_factory: GraphFactory, 
                 graph_extractor: GraphExtractor,
                 graph_frequency_extractor: GraphFrequencyExtractor,
                 LOWER_BOUND=200):
        self.__graph_hasher = graph_hasher
        self.__graph_factory = graph_factory
        self.__graph_extractor = graph_extractor
        self.__graph_frequency_extractor = graph_frequency_extractor
        self.__flow_extractor = flow_extractor
        self.__LOWER_BOUND = LOWER_BOUND
        self.__graph_comparator = GraphComparator()
        self.__graph_grouper = GraphGrouper(compator=self.__graph_comparator)
        self.__graph_operator = GraphOperator(graph_factory)
        
    def extract(self, flows: List[Flow]) -> dict:
        super_flows = []
        flow_graphs = [self.__graph_extractor.extract(flow) \
                       for flow in flows]
        for flow in flows:
            super_flows.extend(self.__flow_extractor.extract_sub_flow(flow))
        frequency_dict, graphs = \
            self.__graph_frequency_extractor.extract(super_flows)
        frequent_graphs = set(graph for graph in graphs \
                          if frequency_dict[self.__graph_hasher.hash(graph)] > \
                              self.__LOWER_BOUND)
        print("length of frequent graph: ", frequent_graphs.__len__())
        sorted_graph = self.__graph_grouper.group(frequent_graphs)
        unique_frequency = self.__count_unique(flow_graphs, sorted_graph)
        result = {k: v for k, v in unique_frequency.items() \
                  if v > self.__LOWER_BOUND}
        return result
        
        
    def __count_unique(self, 
                       graphs: List[Graph], 
                       layers: List[List[Graph]]) -> dict: 
        unique_frequency = {}
        for layer in layers: 
            # Count the number of frequent graph in graphs of flows. 
            for graph in layer: 
                for i in range(len(graphs)):
                    if self.__graph_comparator.compare(graphs[i], graph):
                        # code = self.__graph_hasher.hash(graph)
                        code = graph
                        if code in unique_frequency.keys(): 
                            unique_frequency[code] += 1
                        else: 
                            unique_frequency[code] = 1
            #Remove the existence of graph in this layer
            for graph in layer: 
                for i in range(len(graphs)):
                    if self.__graph_comparator.compare(graphs[i], graph):
                        graphs[i] = self.__graph_operator.subtract(graphs[i], graph)
        return unique_frequency
        