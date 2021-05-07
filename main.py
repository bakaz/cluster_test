# This is a sample Python script.
import os
import pandas as pd
import jieba
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.


def main():
    # 这里先把所有的数据提取出来，要用谁再说？
    panda_list = load_py()
    finance(panda_list['forex.json'])

def load_py():
    path = "data/"
    # def load(path):
    data_list = os.listdir(path)
    panda_list = {}
    for _ in data_list:
        panda_list[_] = pd.read_json(path+_)
    # print(panda_list)
    return panda_list

def finance(finance_data):
    # 这里主要的目的是处理finacedata
    print(finance_data)

def map_finance(finance_data):




if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/