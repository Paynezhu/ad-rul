'''DEMO'''

import h5py
import numpy as np
import pandas as pd
import csv
import tensorflow as tf
import os
import pandas as pd
from utils import merge

initial_RUL = 28030
folderpath = 'E://data//train'
dataset_name = 'test2.csv'

folders = os.listdir(folderpath)
os.chdir(folderpath)
count = 0
for folder in folders:
    os.chdir(folderpath)
    fpath = os.path.realpath(folder)
    print(fpath)
    count += 1
    dataset = merge(fpath, filename='data' + str(count) + '.csv')  # 生成一个



'''

initial_RUL = initial_RUL
vib_list = []
rul_list = []

with open(dataset, 'r') as csvfile:
    reader_csv = csv.reader(csvfile)
    vibration_signal = [row[4] for row in reader_csv]

    rows = int(initial_RUL / 10)

    for item in vibration_signal:
        item = float(item)
        vib_list.append(item)

    arr2 = []
    arr1 = np.array(vib_list, dtype=np.float32)

    # 下面为关键程序，为二维数组实时赋值
    for row in range(rows):
        arr2.append([])
        for i in range(2560 * row + 1, len(vib_list) + 1):
            if i == 2560 * row + 1:
                arr2[row].append(arr1[i - 1])
                arr2[row].append(arr1[i])
            elif i == 0:
                arr2[row].append(arr1[i])
            elif i % 2560 == 0:
                break
            else:
                arr2[row].append(arr1[i])

    arr2 = np.array(arr2, dtype=np.float32)  # 生成的arr2 是一个 2803*2560的数组
    np.savetxt(dataset_name, arr2, delimiter=',')

    dataframe = pd.DataFrame({'vib': vib_list})
    dataframe.to_csv('vib.csv', index=False)

    label_rul = initial_RUL
    for i in range(len(vibration_signal)):
        if i % 2560 == 0:
            label_rul = label_rul - 10
            print(label_rul)
            label_rul = float(label_rul)
            rul_list.append(label_rul)
    dataframe = pd.DataFrame({'rul': rul_list})
    dataframe.to_csv('rul.csv', index=False)
'''






