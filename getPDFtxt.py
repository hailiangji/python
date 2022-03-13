import pdfplumber

file_path = r'C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF\MT-229.pdf'

with pdfplumber.open(file_path) as pdf:
    page = pdf.pages[0]
    print(page.extract_text())