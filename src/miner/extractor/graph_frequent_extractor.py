#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:23:20 2021

@author: quangkhanh
"""

import pandas as pd 
from typing import List
from tqdm import tqdm

from src.conversation import Graph, Flow, Node, Edge
from src.miner.factory import *
from src.miner.hasher import GraphHasher
from src.miner.extractor.graph_extractor import GraphExtractor


class GraphFrequencyExtractor():
    
    def __init__(self, 
                 graph_factory: UserGraphFactory, 
                 graph_hasher: GraphHasher, 
                 graph_extractor: GraphExtractor): 
        self.__graph_factory = graph_factory
        self.__graph_hasher = graph_hasher 
        self.__graph_extractor = graph_extractor
        
    def extract(self, flows: List[Flow]) -> tuple: 
        frequency_dict = {}
        graphs = []
        flow_size = len(flows)
        for i in tqdm(range(flow_size), desc="extracting"):
            flow = flows[i]
            graph = self.__graph_extractor.extract(flow)
            nodes = graph.nodes
            edges = graph.edges
            code = self.__graph_hasher.hash(nodes=nodes, edges=edges)
            if code in frequency_dict.keys():
                frequency_dict[code] += 1
            else: 
                frequency_dict[code] = 1
            graph = self.__graph_factory.graph(nodes, edges)
            graphs.append(graph)
        return (frequency_dict, graphs)
