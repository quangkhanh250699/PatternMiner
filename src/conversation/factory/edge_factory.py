#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:12:10 2021

@author: quangkhanh
"""

from src.conversation.entity.node import Node
from src.conversation.entity.edge import Edge
from src.conversation.factory.factory_base import Factory
from abc import ABCMeta, abstractmethod


class EdgeFactory(Factory, metaclass=ABCMeta):
    
    @abstractmethod
    def edge(self, node_from: Node, node_to: Node) -> Edge:
        pass 
