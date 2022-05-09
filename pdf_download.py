# -*- coding: UTF-8 -*-
"""
File name:    hh.py
Author:       HailiangJi
IDE:          PyCharm
Created time: 2022.05.06 21:32
"""
import time
import requests
file =r"C:\Users\HailiangJi\Desktop\hpj_pdf.txt"
with open(file ,"r" ) as f:
  strfile = f.read()
  indexl = 0
  totallen=len(strfile)
  print("len of file = ",len(strfile))
while True :
    temp=strfile.rfind(".pdf",indexl,totallen)   #查找.pdf
    print(".pdf index =",temp)
    temp1=strfile.rfind('http',indexl,temp)  #查找http
    print("http index =",temp)
    url=strfile[temp1:temp+4]  #网址链接
    file_name = url.split('/')[-1]  # 提取文件标题
    title=strfile[temp-18:temp]
    print("file name = ",file_name)
    print("url = ",url)
    responsepdf = requests.get(url)
    print(responsepdf.status_code)
    if responsepdf.status_code ==200:
      with open(r"D:\{}.pdf".format(file_name[:-4]), "wb") as code:
        code.write(responsepdf.content)
        time.sleep(5)  # 防止访问速度过快
        print("current pdf download done")
    totallen = temp1
    if temp == -1 :
        print("download complete")
        break
