import pandas as pd
import numpy as np
import os
import json
import re
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

jsonData = []
with open('modcloth_final_data.json') as f:
    for line in f.readlines():
        jsonData.append(json.loads(line))
modcloth_data = pd.DataFrame(jsonData)

def height_converter(x):
    '''converts heights'''
    if pd.isna(x):
        return x
    else:
        split_x = x.split('ft')
        h_to_str = int(split_x[0]) * 12
        if len(split_x) == 2:
            if split_x[1] == '':
                pass
            else:
                h_to_str=h_to_str+int(split_x[1].split('in')[0])

        return height_in_inches_converted_from_string


modcloth_data['height'] = modcloth_data['height'].apply(height_converter)

csv_sets = pd.read_csv('sets.csv')
csv_colors = pd.read_csv('colors.csv')
iventories_df = pd.read_csv('inventories.csv')
inventories_part_df = pd.read_csv('inventory_parts.csv')
parts_and_colors_df = inventories_part_df.merge(
    csv_colors, left_on='color_id', right_on='id', how='inner'
)
pcs_df = parts_and_colors_df.merge(
    iventories_df, left_on='inventory_id', right_on='id', how='inner'
)
pcsiv_df = pcs_df.merge(
    csv_sets, left_on='set_num', right_on='set_num', how='inner'
)
data = pd.pivot_table(
    data=pcsiv_df, values='rgb', index='year', aggfunc="nunique"
)
plt.plot(data)
plt.axvline(x = 2004, c = 'r')
plt.ylabel('unique colors per year')
