#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:36:18 2021

@author: quangkhanh
"""
from abc import ABCMeta, abstractmethod

class Hasher:
    @abstractmethod
    def hash(self, *args):
        pass

