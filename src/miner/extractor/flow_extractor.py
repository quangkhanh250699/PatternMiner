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
    
    def __init__(self): 
        self.__flow_factory = UserFlowFactory()

    def extract(self, file_path: str) -> List[Flow]:
        '''
        Extract a csv file to get list of flows.

        Parameters
        ----------
        file_path : str
            csv file containing actions.

        Returns
        -------
        List[Flow]
            List of Flows.

        '''
        df = pd.read_csv(file_path)
        df[FlowExtractor.__action_col] = df[FlowExtractor.__action_col] \
            .fillna(FlowExtractor.__nan_action)
        flows = [] 
        for index, frame in df.groupby(FlowExtractor.__message_id):
            str_flow = frame.user_action.to_list()
            flow = self._make_flow(str_flow)
            flows.append(flow)
        return flows
    
    def extract_sub_flow(self, flow: Flow, 
                         n_messages=[6, 5, 4, 3, 2]) -> List[Flow]:
        '''
        Extract subset actions of actions in the flow

        Parameters
        ----------
        flow : Flow
            Based flow.

        Returns
        -------
        List[Flow]
            List of sub-flows.

        '''
        result = []
        for n in n_messages:
            if flow.flow.__len__() > n: 
                for i in range(flow.flow.__len__() - n + 1):
                    sub_flow = self.__make_flow(flow.flow[i:(i+n)])
                    result.append(sub_flow)
        return result
    
    def _make_flow(self, str_flow: List[str]) -> Flow: 
        reduced_flow = self.__reduce_flow(str_flow)
        return self.__flow_factory.flow(reduced_flow)
    
    def __reduce_flow(self, flow: List[str]):
        '''
        Reduce sequence of consecutive identical actions to one.
        For example: 
            shop_turn -> shop_turn -> shop_turn 
        will be turned to "shop_turn"

        Parameters
        ----------
        flow : List[str]
            flow of actions.

        Returns
        -------
        reduced_flow : List[str]

        '''
        reduced_flow = []
        emerge = False 
        last_action = None
        for i in range(flow.__len__()):
            if flow[i] is not last_action:
                last_action = flow[i]
                reduced_flow.append(last_action)
        return reduced_flow
        