'''AUTHOR :PEIYUAN
   FUNCTION :做一些基本函数的定义工作包含：
     1.文件夹中csv的合并
     2.合并文件后的RUL计算
     3.轴承二维振动信号数组制作和剩余寿命标签数据集制作（以行数对应）'''

import os
import glob
import csv
import tensorflow as tf
import numpy as np
import pandas as pd





def merge(inputfolder,filename):
    '''融合一个文件夹下面的数据,生成的文件是路径下
    每个文件夹中都有以data+number.csv为文件名的csv文件
    foladerpath要将所有轴承训练数据集的数据全部放进去，例如：E:\\data\\train'''
    Folder_Path = inputfolder  # 要拼接的文件夹及其完整路径，注意不要包含中文
    SaveFile_Name = filename  # 合并后要保存的文件名
    os.chdir(Folder_Path)    #输出的数据类型不对  其改变了数据类型
    csv_list = glob.glob(Folder_Path + '\\'+'*.csv')    #文件夹中遍历csv文件
    print("一共发现%s个文件" % len(csv_list))
    item = 0
    for i in csv_list:
        fr = open(i, 'r').read()
        item+=1
        with open(SaveFile_Name, 'a') as f:
            if item%100 ==0:
                print("the number is %d" %item)
            f.write(fr)
    print("merge finish")
    return SaveFile_Name




def initial_RUL(raw_data):
    '''对每个数据集的初始RUL进行计算'''
    filepath = os.path.abspath(raw_data)
    filelength = len(open(filepath, 'rU').readlines())
    initial_RUL = 10 * (filelength / 2560)
    return initial_RUL




def pre_dataset(raw_data, initial_RUL,dataset_name):
    '''raw_data是一个包含轴承全部运行信号的合并文件
    准备训练数据集和标签数据集,目的是生成
    一个(RUL/10)*2560的初始矩阵,命名为dataset_name
    一个剩余寿命标签集rul.csv
    一个一维振动信号数组vib.csv
    '''


    initial_RUL = initial_RUL
    vib_list = []
    rul_list = []

    with open(raw_data,'r') as csvfile:

        reader_csv = csv.reader(csvfile)
        vibration_signal = [row[4] for row in reader_csv]

        rows = int(initial_RUL/10)


        for item in vibration_signal:
            item = float(item)
            vib_list.append(item)


        arr2=[]
        arr1= np.array(vib_list,dtype=np.float32)

        #下面为关键程序，为二维数组实时赋值
        for row in range(rows):
            arr2.append([])
            for i in range(2560*row+1,len(vib_list)+1):
                if i==2560*row+1:
                    arr2[row].append(arr1[i-1])
                    arr2[row].append(arr1[i])
                elif i==0:
                    arr2[row].append(arr1[i])
                elif i%2560 == 0:
                    break
                else:
                    arr2[row].append(arr1[i])

        arr2 = np.array(arr2,dtype=np.float32)    #生成的arr2 是一个 2803*2560的数组
        np.savetxt(dataset_name, arr2, delimiter=',')



        dataframe = pd.DataFrame({'vib':vib_list})
        dataframe.to_csv('vib.csv',index=False)



        label_rul = initial_RUL
        for i in range(len(vibration_signal)):
            if i%2560==0:
                label_rul = label_rul -10
                print(label_rul)
                label_rul = float(label_rul)
                rul_list.append(label_rul)
        dataframe = pd.DataFrame({'rul':rul_list})
        dataframe.to_csv('rul.csv',index=False)

    return arr2,rul_list



'''此部分为运行merge之前必须要经过的部分'''
if __name__ == '__main__':
    folderpath = ('E:\\data\\train')
    folders = os.listdir(folderpath)
    os.chdir(folderpath)
    count = 0
    for folder in folders:
        os.chdir(folderpath)
        fpath = os.path.realpath(folder)
        print(fpath)
        count += 1
        dataset = merge(fpath, filename='data'+str(count)+'.csv')


