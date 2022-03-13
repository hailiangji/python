import os
src = r"C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF\MT-0010.pdf"
dst = r"C:\Users\HailiangJi\Desktop\ADI-混合信号电子系统PDF\MT-001.pdf"
os.rename(src,dst)
print("重命名完毕")