# -*- coding: utf-8 -*-
import csv
import numpy as np
import pandas as pd
file_dir = r'C:\Users\HailiangJi\python\aa.csv'
df = pd.read_csv(file_dir,sep=" ",encoding = 'gb2312')
df.to_csv(index=False)
print(df.columns)

print(df)