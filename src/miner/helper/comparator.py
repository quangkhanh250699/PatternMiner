#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:42:47 2021

@author: quangkhanh
"""

from abc import ABCMeta, abstractmethod


class Comparator(metaclass=ABCMeta):
    
    @abstractmethod
    def compare(self, element1, element2) -> bool: 
        pass 
