#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:05:43 2021

@author: quangkhanh
"""

from src.miner.extractor import FlowExtractor

import pandas as pd

def transform_flow(flow: list, substitute: dict):
    transformed_flow = []
    for act in flow: 
        if act in substitute.keys():
            transformed_flow.append(substitute[act])
        else: 
            transformed_flow.append(act)
    return transformed_flow

def split_flow_to_turns(flow: list):
    request = "request"
    social_act = "social_act"
    shop_turn = "shop_turn"
    turns = []
    i = 0
    while (i < len(flow)): 
        if flow[i] == request: 
            is_replied = False
            this_turn = [flow[i]]
            i += 1
            while(i < len(flow)):
                if flow[i] == social_act: 
                    if i + 1 < len(flow): 
                        if flow[i + 1] == shop_turn: 
                            i += 2
                        else: 
                            i += 1
                    else: 
                        i += 1
                elif flow[i] == request and is_replied: 
                    turns.append(this_turn)
                    break
                else: 
                    if flow[i] == shop_turn: 
                        is_replied = True
                    this_turn.append(flow[i])
                    i += 1
                if i >= len(flow): 
                    turns.append(this_turn)
        else: 
            i += 1
    return turns
    

data_path = "data/actions.csv"


substitute = {
"ask_availability#size": "request", 
"ask_if_sells#size": "request",
"ask_is_bot": "request",
"request#price": "request",
"greet": "social_act",
"thank": "social_act", 
"agree": "social_act"
}

flow_extractor = FlowExtractor()

df = pd.read_csv(data_path)

df["user_action"] = df["user_action"].fillna("shop_turn")

mapper = {}
flows = []
count = 0
for index, frame in df.groupby("message_id"):
            str_flow = frame.user_action.to_list()
            str_flow = transform_flow(str_flow, substitute)
            flow = flow_extractor._make_flow(str_flow)
            flows.append(flow)
            mapper[count] = index
            count += 1
            
turns = [split_flow_to_turns(flow.flow) for flow in flows]

#%% 
count_shop_turns = []
for turn in turns: 
    count = [x.count('shop_turn') for x in turn]
    count_shop_turns.append(count)

#%%

value = [0] * 10
for count_turn in count_shop_turns: 
    for c in count_turn:
        value[c] += 1
        
#%% 

import matplotlib.pyplot as plt

plt.bar(x=range(len(value)), height=value)
plt.xlabel("the number of shop turns")
plt.ylabel("the number of requests")
plt.title("number of shop turns distribution")
plt.show()

#%% 

import numpy as np 

total_turns = sum(value[1:])
data = np.array(value[1:]) / total_turns
plt.bar(x=range(1, data.shape[0] + 1), height=data)
plt.xlabel("the number of shop turns")
plt.ylabel("proportion")
plt.title("number of shop turns distribution")
plt.show()

#%% 

from scipy.optimize import curve_fit

def dist_func(x, p):
    return (1 - p) ** (x - 1) * p

xdata = np.array(range(1, len(data) + 1))
ydata = data

popt, pcov = curve_fit(dist_func, xdata, ydata)

#%%

p = popt[0]
fit_data = dist_func(xdata, p)

plt.bar(x=range(1, data.shape[0] + 1), height=data)
plt.plot(xdata, fit_data, 'x-r', label="p = {}".format(round(p, 2)))
plt.xlabel("the number of shop turns")
plt.ylabel("the number of conversations")
plt.title("number of shop turns distribution")
plt.legend()
plt.show()