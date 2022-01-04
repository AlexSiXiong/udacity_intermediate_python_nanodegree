import pandas as pd
import json
from collections import Counter

df = pd.DataFrame()

filename = 'data/neos.csv'


chunksize = 1e6
for chunk in pd.read_csv(filename, chunksize=chunksize):
    df = df.append(chunk)

print(len(df))
print(df['pdes'][0])
print(len(df[df['name'] == 'IAU']))
print(df.columns.values)
print(df.diameter.isna().sum())
print(df['diameter'][:50])
#
# def load_json(filename='./data/cad.json'):
#     with open(filename) as f:
#         return json.load(f)
#
#
# data = load_json()
# print(data['count'])
#
# for i in data['data']:
#     #     if i[0] == '2015 CL':
#     #         if i[3].split(' ')[0] == '2000-Jan-01':
#     #             print(i[4], i[5], i[6])
#     #             break
#
#     if i[0] == '2002 PB':
#         if i[3].split(' ')[0] == '2000-Jan-01':
#             print(i[7], i[8])
#             break

