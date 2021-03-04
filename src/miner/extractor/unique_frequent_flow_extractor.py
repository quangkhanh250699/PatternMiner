#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:14:50 2021

@author: quangkhanh
"""

from src.conversation import Flow
from src.miner.factory import UserFlowFactory
from src.miner.hasher import FlowHasher
from src.miner.extractor.frequent_flow_extractor import \
    FrequentFlowExtractor, SubflowExtractor
from src.miner.helper import Grouper, FlowComparator

from typing import List
from tqdm import tqdm


class UniqueFrequentFlowExtractor:
    
    def __init__(self, 
                 flow_hasher: FlowHasher,
                 flow_grouper: Grouper,
                 frequent_flow_extractor: FrequentFlowExtractor, 
                 MIN_PROPORTION = 0.03):
        self.__flow_hasher = flow_hasher
        self.__frequent_flow_extractor = frequent_flow_extractor
        self.__flow_grouper = flow_grouper
        self.__MIN_PROPORTION = MIN_PROPORTION
    
    def extract(self, flows: List[Flow]) -> dict:
        return self._extract(flows)
        
    def _extract(self, flows: List[Flow]) -> dict:
        frequency = self.__frequent_flow_extractor.extract(flows)
        min_count = int(len(flows) * self.__MIN_PROPORTION)
        high_frequency = {flow:f for flow, f in frequency.items() 
                          if f > min_count}
        layers = self.__flow_grouper.group([k for k in high_frequency.keys()])
        unique_high_frequency = self.__extract_unique(flows, layers)
        return {k:v for k, v in unique_high_frequency.items() if v > min_count}
        
    def __extract_unique(self,
                         flows: List[Flow], 
                         layers: List[List[Flow]]):
        flow_codes = [self.__flow_hasher.hash(flow=flow) for flow in flows]
        size = len(flow_codes)
        unique_frequency = {}
        for k in tqdm(range(len(layers)), desc="extracting in layer"):
            # in the non-dominated layer
            
            # count the frequency of each flow
            for frequent_flow in layers[k]:
                count = 0
                current_flow_code = self.__flow_hasher.hash(flow=frequent_flow)
                for i in range(size):
                    if current_flow_code in flow_codes[i]:
                        count += 1
                unique_frequency[frequent_flow] = count
            
            # remove the existence of each flow
            for frequent_flow in layers[k]:
                current_flow_code = self.__flow_hasher.hash(flow=frequent_flow)
                for i in range(size):
                    if current_flow_code in flow_codes[i]:
                        flow_codes[i].replace(current_flow_code, "$")
                        
        return unique_frequency
        
    
    class Builder:
        def __init__(self):
            flow_comparator = FlowComparator()
            flow_factory = UserFlowFactory()
            subflow_extractor = SubflowExtractor(flow_factory)
            self.__flow_hasher = FlowHasher()
            self.__grouper = Grouper(flow_comparator)
            self.__frequent_flow_extractor = \
                FrequentFlowExtractor(flow_factory,
                                      subflow_extractor)
            self.__MIN_PROPORTION = 0.03
        
        def build(self): 
            return UniqueFrequentFlowExtractor(self.__flow_hasher,
                                               self.__grouper,
                                               self.__frequent_flow_extractor,
                                               self.__MIN_PROPORTION)
        
        def set_hasher(self, hasher: FlowHasher): 
            self.__flow_hasher = hasher
            return self 
        
        def set_grouper(self, grouper: Grouper):
            self.__grouper = grouper
            return self
            
        def set_frequent_flow_extractor(self, 
                                        frequent_flow_extractor: FrequentFlowExtractor):
            self.__frequent_flow_extractor = frequent_flow_extractor
            return self 
        
        def set_min_proportion(self, MIN_PROPORTION):
            self.__MIN_PROPORTION = MIN_PROPORTION
            return self 
