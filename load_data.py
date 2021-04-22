import os
import pandas as pd

path = "data"
# def load(path):

    read_data = pd.read_json("data/"+path)
    print(read_data)