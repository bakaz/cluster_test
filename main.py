# This is a sample Python script.
import os
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.


def main():
    load_py()
    return 0

def load_py():
    path = "data"
    # def load(path):

    read_data = pd.read_json("data/" + path)
    print(read_data)

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/