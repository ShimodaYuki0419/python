import pandas as pd
import glob

csv_pathlist = glob.glob(r'csv/*.csv')
data_list = []
print(csv_pathlist)

for csv in csv_pathlist:
    data_list.append(pd.read_csv(csv,encoding="cp932"))
    df = pd.concat(data_list)
    df.to_csv('total.csv',encoding='utf-8_sig')
