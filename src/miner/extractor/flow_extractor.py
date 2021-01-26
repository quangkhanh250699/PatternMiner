#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:29:40 2021

@author: quangkhanh
"""
import pandas as pd 
from typing import List

from src.conversation import Flow
from src.miner.factory import UserFlowFactory


class FlowExtractor(): 
    
    __message_id = "message_id"
    __action_col = "user_action"
    __nan_action = "shop_turn"
    
    __n_messages = [6, 5, 4, 3, 2]
    
    def __init__(self): 
        self.__flow_factory = UserFlowFactory()

    def extract(self, file_path: str) -> List[Flow]:
        df = pd.read_csv(file_path)
        df[FlowExtractor.__action_col] = df[FlowExtractor.__action_col] \
            .fillna(FlowExtractor.__nan_action)
        flows = [] 
        for index, frame in df.groupby(FlowExtractor.__message_id):
            str_flow = [index] + frame.user_action.to_list()
            flow = self.__make_flow(str_flow)
            flows.append(flow)
        return flows
    
    def extract_sub_flow(self, flow: Flow) -> List[Flow]:
        result = []
        for n in FlowExtractor.__n_messages:
            if flow.flow.__len__() > n: 
                for i in range(flow.flow.__len__() - n + 1):
                    sub_flow = self.__make_flow(flow.flow[i:(i+n)])
                    result.append(sub_flow)
        return result
    
    def __make_flow(self, str_flow: List[str]) -> Flow: 
        reduced_flow = self.__reduce_flow(str_flow)
        return self.__flow_factory.flow(reduced_flow)
    
    def __reduce_flow(self, flow: List[str]):
        reduced_flow = []
        emerge = False 
        for i in range(flow.__len__()):
            if flow[i] == FlowExtractor.__nan_action:
                if not emerge:
                    reduced_flow.append(flow[i]) 
                    emerge = True
            else: 
                reduced_flow.append(flow[i])
                emerge = False
        return reduced_flow
        