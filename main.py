# This is a sample Python script.
import os
import pandas as pd
import jieba
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

switch_type = 0

def main():
    # 这里先把所有的数据提取出来，要用谁再说？
    panda_list = load_py()
    # finance(panda_list['forex.json'])
    sava_py(panda_list['forex.json'])

def load_py():
    path = "data/"
    # def load(path):
    data_list = os.listdir(path)
    panda_list = {}
    for _ in data_list:
        panda_list[_] = pd.read_json(path+_)
    # print(panda_list)
    return panda_list

def sava_py(save_data):
    # title = save_data['title']
    # time = save_data['post_time']
    # content = save_data['content']
    # title存放
    global switch_type
    title_content = save_data[['title', 'content']]
    switch_type = 1
    title_content_temp = title_content.apply(pdtotxt)
    time_content = save_data[['post_time', 'content']]
    switch_type = 2
    time_content_temp = time_content.apply(pdtotxt)
    # if os.path.exists()
    # print(title)
    # print(type(title))

def pdtotxt(pd_data):
    # 如果这里是1就是title，如果是2就是posttime
    global switch_type
    if switch_type == 1:
        if not os.path.isdir('title'):
            os.mkdir('title')
        txt_id = pd_data['title']
        file = open(txt_id,'w')
        file.write(pd_data['content'])
        file.close()
    elif switch_type == 2:
        if not os.path.isdir('post_time'):
            os.mkdir('post_time')
        txt_id = pd_data['post_time']
        file = open(txt_id,'w')
        file.write(pd_data['content'])
        file.close()
    return pd_data

    return

# def finance(finance_data):
#     # 这里主要的目的是处理finacedata
#     # print(finance_data)
#     title_content = finance_data[['title','content']]
#     time_content = finance_data[['post_time','content']]
#     print(title)
#     print(type(title))
#     return

def map_finance(finance_data):

    return


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/