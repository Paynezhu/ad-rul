import numpy as np
import os
import tensorflow as tf
import pandas as pd
from utils import initial_RUL,pre_dataset
import time

raw_data = 'data5.csv'
starttime = time.clock()
RUL = initial_RUL(raw_data)
arr2, rul_list = pre_dataset(raw_data,RUL,dataset_name = 'test5.csv')
endtime = time.clock()
print(endtime - starttime)