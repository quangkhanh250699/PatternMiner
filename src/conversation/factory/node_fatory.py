#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:12:19 2021

@author: quangkhanh
"""

from src.conversation.entity.node import Node
from src.conversation.factory.factory_base import Factory

from abc import ABCMeta, abstractmethod


class NodeFactory(Factory, metaclass=ABCMeta):
    
    @abstractmethod
    def node(self, name: str) -> Node:
        pass 
