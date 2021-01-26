#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:12:01 2021

@author: quangkhanh
"""

from src.conversation.entity.graph import Graph
from src.conversation.factory.factory_base import Factory

from abc import ABCMeta, abstractmethod 


class GraphFactory(Factory, metaclass=ABCMeta):
    
    @abstractmethod 
    def graph(self, nodes, edges) -> Graph:
        pass
