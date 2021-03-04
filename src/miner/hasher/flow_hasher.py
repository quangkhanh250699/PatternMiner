#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:00:46 2021

@author: quangkhanh
"""

from src.miner.hasher.hasher_base import Hasher
from src.conversation import Flow


class FlowHasher(Hasher):
        
    def hash(self, flow=None, str_list=None):
        _codes = []
        if flow is not None: 
            _codes = flow.flow
        elif str_list is not None: 
            _codes = str_list 
        else: 
            raise Exception("Input is wrong!")
        
        return "->".join(_codes)
