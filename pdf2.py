import os
import re

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

dir_path = r"D:\test"


def parses(path):
    with open(path, 'rb') as fp:

        # 创建PDF资源管理器
        resource = PDFResourceManager()
        # 参数分析器
        laparam = LAParams()
        # 创建聚合器
        device = PDFPageAggregator(resource, laparams=laparam)
        # 页面解释器
        interpreter = PDFPageInterpreter(resource, device)
        pages = PDFPage.get_pages(fp)
        for page in pages:
            interpreter.process_page(page)
            # 使用聚合器获得内容
            layout = device.get_result()
            for out in layout:
                if hasattr(out, "get_text"):
                    # 打印pdf文件内容
                    # print(out.get_text())
                    if re.search("^名 (.*)", out.get_text()):
                        result = re.search("^名 (.*)", out.get_text())
                        return result.group(1)


for i in os.listdir(dir_path):
    file_path = os.path.join(dir_path, i)
    if os.path.isfile(file_path) and str(file_path).endswith("pdf"):
        new_name = parses(file_path)
        print("{:*^30}".format(f"{file_path}分割符号"))
        os.rename(file_path, os.path.join(dir_path, f"{new_name}.pdf"))