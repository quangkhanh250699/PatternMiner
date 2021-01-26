#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 15:13:07 2021

@author: quangkhanh
"""

class Node(): 
    
    __name: str
    
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name