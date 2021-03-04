#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:04:27 2021

@author: quangkhanh
"""

import pandas as pd

from src.miner.hasher import GraphHasher, EdgeHasher, NodeHasher
from src.miner.factory import UserEdgeFactory, UserFlowFactory, \
    UserGraphFactory, UserNodeFactory
from src.miner.extractor import FlowExtractor, GraphFrequencyExtractor, \
    UniqueFrequentExtractor, GraphExtractor
    
UNIQUE_SUPPORT = 400
    
node_hasher = NodeHasher()
edge_hasher = EdgeHasher(node_hasher)
graph_hasher = GraphHasher(node_hasher, edge_hasher)
node_factory = UserNodeFactory()
edge_factory = UserEdgeFactory(edge_hasher)
graph_factory = UserGraphFactory(graph_hasher)
flow_factory = UserFlowFactory()
flow_extractor = FlowExtractor()
graph_extractor = GraphExtractor(graph_factory,
                                 edge_factory,
                                 node_factory)
graph_frequency_extractor = GraphFrequencyExtractor(graph_factory,
                                                   graph_hasher,
                                                   graph_extractor)

unique_graph_extractor = UniqueFrequentExtractor(flow_extractor,
                                                 graph_hasher,
                                                 graph_factory,
                                                 graph_extractor,
                                                 graph_frequency_extractor, 
                                                 LOWER_BOUND=UNIQUE_SUPPORT)
