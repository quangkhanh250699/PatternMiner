#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:47:50 2021

@author: quangkhanh
"""

from src.conversation import Flow
from src.conversation import FlowFactory
from src.miner.extractor.subflow_extractor import SubflowExtractor

from typing import List, Set
from tqdm import tqdm


class FrequentFlowExtractor: 
    
    def __init__(self, 
                 flow_factory: FlowFactory, 
                 subflow_extractor: SubflowExtractor,
                 max_length=6,
                 min_length=2):
        # self.__flow_hasher = flow_hasher
        self.__flow_factory = flow_factory
        self.__subflow_extractor = subflow_extractor
        self.__min_length = min_length
        self.__max_length = max_length
        
    def extract(self, flows: List[Flow]) -> dict: 
        subflow_sets = self.__make_subsets(flows)
        frequency_dict = self.__calculate_frequency(subflow_sets)
        return frequency_dict
            
    def __calculate_frequency(self, subflows: List[Set[Flow]]) -> dict: 
        size = len(subflows)
        frequency = {}
        for i in tqdm(range(size), desc="counting"):
            subflow_set = subflows[i]
            for subflow in subflow_set:
                if subflow in frequency.keys():
                    continue 
                else: 
                    count = 1
                    for j in range(size):
                        if i == j: 
                            continue
                        else: 
                            other_set = subflows[j]
                            if subflow in other_set: 
                                count += 1
                    frequency[subflow] = count
        return frequency    
                
    def __make_subsets(self, flows: List[Flow]) -> List[Set[Flow]]:
        '''
        Get all subflows of flows.  Each set of subflows corresponds to a flow.

        Parameters
        ----------
        flows : List[Flow]
            List of based flows.

        Returns
        -------
        List[set]
            List of subflows set corresponding to a flow.

        '''
        all_subsets = []
        for flow in flows:
            sub_flows = []
            for length in range(self.__min_length, self.__max_length+1):
                sub_flows.extend(self.__subflow_extractor.extract(flow, length))
            all_subsets.append(set(sub_flows))
        return all_subsets
        