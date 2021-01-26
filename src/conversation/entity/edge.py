#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:10:21 2021

@author: quangkhanh
"""

from src.conversation.entity.node import Node


class Edge:
    __node_from: Node
    __node_to: Node

    def __init__(self, node_from, node_to):
        self.__node_from = node_from
        self.__node_to = node_to

    @property
    def node_from(self):
        return self.__node_from

    @property
    def node_to(self):
        return self.__node_to
