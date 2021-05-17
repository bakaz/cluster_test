import os
import pandas as pd
import codecs


path = "data/"
# def load(path):
data_list = os.listdir(path)
panda_list = {}
for _ in data_list:
    panda_list[_] = pd.read_json(path + _)
finance_data = panda_list['finance.json']
forex_data = panda_list['forex.json']
fund_data = panda_list['fund.json']
futures_data = panda_list['futures.json']
global_data = panda_list['global.json']
other_data = panda_list['other.json']
stock_data = panda_list['stock.json']
print(finance_data['content'][1])

for k, v in panda_list.items():
    print(v)
    for i in range(len(v)):

        # print(i)