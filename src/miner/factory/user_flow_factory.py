#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:09:03 2021

@author: quangkhanh
"""

from src.conversation import Flow, FlowFactory
from src.miner.hasher import FlowHasher

from typing import List


class UserFlowFactory(FlowFactory): 
    
    __map: dict
    
    def __init__(self,
                 flow_hasher=FlowHasher()):
        self.__map = dict()
        self.__flow_hasher = flow_hasher
    
    def flow(self, flow: List[str]) -> Flow:
        code = self.__flow_hasher.hash(str_list=flow)
        if self.contain(code): 
            return self.__map[code]
        else: 
            new_flow = Flow(flow)
            self.__map[code] = new_flow 
            return new_flow

    def contain(self, code: str) -> bool:
        return code in self.__map.keys()

    def count(self) -> int:
        return self.__map.__len__()
    
    def to_list(self):
        return list(self.__map.values())