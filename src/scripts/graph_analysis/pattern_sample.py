from src.scripts.graph_analysis.base_entity import * 
#%% 
flows = flow_extractor.extract("data/actions.csv")
result = unique_graph_extractor.extract(flows)


#%%
patterns = [graph_hasher.hash(graph) for graph in result.keys()]
pattern_id = {v:k for k, v in enumerate(patterns)}

#%% 
import pandas as pd 
from src.miner.helper.graph_comparator import GraphComparator

N_SAMPLE = 10

actions = pd.read_csv("data/actions.csv")
actions.user_action = actions.user_action.fillna("shop_turn")

pattern_graphs = list(result.keys())
comparator = GraphComparator()
pattern_samples = {}

for pattern in pattern_graphs: 
    pattern_samples[pattern] = []

for index, frame in actions.groupby("message_id"):
    for pattern in pattern_graphs:
        if len(pattern_samples[pattern]) > N_SAMPLE:
            continue
        str_flow = frame.user_action.to_list()
        flow = flow_extractor._make_flow(str_flow)
        graph = graph_extractor.extract(flow)
        if comparator.compare(graph, pattern): 
            pattern_samples[pattern].append(index)
        
