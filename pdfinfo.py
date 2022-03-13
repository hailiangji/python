#-*- coding: utf-8 -*-
import time
import re
import PyPDF2
import pdfplumber
import sys
import os
filedir = r'C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF'
testfile = r'C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF\MT-001.pdf'
def extract_content(pdf_path):
    # 内容提取，使用 pdfplumber 打开 PDF，用于提取文本
    #with pdfplumber.open(pdf_path) as pdf_file:
        # 使用 PyPDF2 打开 PDF 用于提取图片
    try:
        f=open(pdf_path, "rb")
        pdf = PyPDF2.PdfFileReader(f)
        pdfinfo=dict(pdf.getDocumentInfo()) #将读取出来的
        test=pdf.getPageLayout()
        print("getoutlines ",test)
        for content in (pdfinfo) : # content <class 'PyPDF2.generic.NameObject'>
            print("{} =".format(str(content)),pdfinfo["{}".format(str(content))])
            if str(content).find('/Title') == 0 :
                title = str(pdfinfo["{}".format(str(content))])
                newtitle=re.sub('[\/:*?"<>|]', ' ', title)#使用空格替代
                filename =os.path.dirname(os.path.realpath(pdf_path)) + '\\'+newtitle +'.pdf'
                print('new filename',filename)
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        f.close()
        #os.rename(pdf_path, filename) #替换名字
    except Exception as err:
        print("error info {}".format(err))
    return pdfinfo  #返回文件信息，字典形式

if __name__ == "__main__":
    extract_content(r'C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF\MT-229.pdf')
