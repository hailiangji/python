#-*- coding: utf-8 -*-
import PyPDF2
import pdfplumber
import sys
def extract_content(pdf_path):
    # 内容提取，使用 pdfplumber 打开 PDF，用于提取文本
    with pdfplumber.open(pdf_path) as pdf_file:
        # 使用 PyPDF2 打开 PDF 用于提取图片
        pdf_image_reader = PyPDF2.PdfFileReader(open(pdf_path, "rb"))
        pdfinfo=dict(pdf_image_reader.getDocumentInfo()) #将读取出来的
        for content in (pdfinfo) :
            print("{} =".format(str(content)),pdfinfo["{}".format(str(content))])
        print("  ")
        print("  ")
        if not sys.warnoptions:
            print("eeeeeee")
            import warnings
            warnings.simplefilter("ignore")
    return pdfinfo  #返回文件信息，字典形式

if __name__ == "__main__":
    extract_content(r'E:\WORK\Datasheet\__Study\_Book\ADI-混合信号电子系统PDF\MT-001.pdf')