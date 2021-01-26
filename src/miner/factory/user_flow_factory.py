#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:11:48 2021

@author: quangkhanh
"""

from src.conversation import Flow, FlowFactory

from typing import List 


class UserFlowFactory(FlowFactory):
    
    def flow(self, flow: List[str]) -> Flow: 
        return Flow(flow)
