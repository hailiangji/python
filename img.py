# 使用matplotlib.pyplot
imagePath = r"E:\WORK\_Sigtrum\__Board\Jiawarenan\Fab2\HWdebug\1.bmp"
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(threshold=np.inf) # threshold 指定超过多少使用省略号，np.inf代表无限大

#img1 = plt.imread(imagePath)# print type:
img1=np.array(Image.open(imagePath).convert('L'))
# print(len(img1[0]))
# print(len(img1[0][0]))
# print((img1[0]))
with open('tt.txt','a+') as file :
    file.write(str(img1))
file.close()
#for x in range

print(type(img1))
print('image shape',img1.shape)
print('image ndim',img1.ndim)

print('image size',img1.size)
print('image dtype',img1.dtype)
arr=img1.flatten()
# n, bins, patches = plt.hist(arr, bins=256, facecolor='green', alpha=0.75)
# plt.show()
src=Image.open(imagePath)
r , g ,b =src.split()

plt.subplot(3,1,1)
ar=np.array(r).flatten()
plt.hist(ar, bins=256, density =1,facecolor='r',edgecolor='r')
plt.imshow(ar)

plt.subplot(3,1,2)
ag=np.array(g).flatten()
plt.hist(ag, bins=256, density =1, facecolor='g',edgecolor='g')
plt.imshow(ag)

plt.subplot(3,1,3)
ab=np.array(b).flatten()
plt.hist(ab, bins=256, density =1, facecolor='b',edgecolor='b')
plt.imshow(ab)
plt.show()
#plt.imshow(img1)
