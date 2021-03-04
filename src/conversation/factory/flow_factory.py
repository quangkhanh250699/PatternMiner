#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:07:12 2021

@author: quangkhanh
"""

from src.conversation.factory.factory_base import Factory
from src.conversation.entity.flow import Flow

from abc import ABCMeta, abstractmethod
from typing import List 


class FlowFactory(metaclass=ABCMeta): 
    
    @abstractmethod
    def flow(self, flow: List[str]) -> Flow:
        pass
    
    @abstractmethod
    def contain(self, code: str) -> bool: 
        pass 
    
    @abstractmethod
    def to_list(self):
        pass 
    
    @abstractmethod 
    def count(self):
        pass