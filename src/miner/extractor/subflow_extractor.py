#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 10:55:42 2021

@author: quangkhanh
"""

from src.conversation import Flow, FlowFactory
from src.miner.hasher import FlowHasher
from typing import List 


class SubflowExtractor:
    
    def __init__(self,
                 flow_factory: FlowFactory): 
        self.__flow_factory = flow_factory
    
    def extract(self, flow: Flow, size=3) -> List[Flow]: 
        '''
        Extract all sub-flow of a flow

        Parameters
        ----------
        flow : Flow
            based flow
        size : int, optional
            number of actions in a sub-flow. The default is 3.

        Returns
        -------
        List[Flow]
            sub-flow of based flow.

        '''
        flow_lenght = len(flow.flow)
        sub_flows = set()
        for i in range(flow_lenght - size):
            sub_str = flow.flow[i:i+size]
            sub_flow = self.__flow_factory.flow(sub_str)
            sub_flows.add(sub_flow)
        return list(sub_flows)
