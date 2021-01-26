#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:03:37 2021

@author: quangkhanh
"""
from typing import List


class Flow: 
    
    __flow: List[str]
    
    def __init__(self, flow: List[str]): 
        self.__flow = flow
        
        
    @property
    def flow(self): 
        return self.__flow
