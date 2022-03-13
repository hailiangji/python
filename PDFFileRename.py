import oswalk
import pdfinfo

file_dir = r"C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF"

if __name__ == '__main__' :
    filefullname, filename =oswalk.file_name(file_dir)
    for fileOrgName in filefullname :
        pdfinfo.extract_content(fileOrgName)
    print("PDF file name update done!")