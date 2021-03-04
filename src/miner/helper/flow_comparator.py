#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:44:33 2021

@author: quangkhanh
"""

from src.conversation import Flow
from src.miner.helper.comparator import Comparator
from src.miner.hasher import FlowHasher


class FlowComparator(Comparator):
    
    def __init__(self):
        self.__flow_hasher = FlowHasher()
    
    def compare(self, element1: Flow, element2: Flow) -> bool:
        flow1 = self.__flow_hasher.hash(flow=element1)
        flow2 = self.__flow_hasher.hash(flow=element2)
        return ((flow2 in flow1) and (len(flow1) > len(flow2)))
