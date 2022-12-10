# this is the test for function call
#接收多个返回值
def my_fun(a,b,c):
    x=a+b
    y=b+c
    z=a*b*c
    return x,y,z

x, y, z = my_fun(1,2,3)
print(x)
print(y)
print(z)

import sys
import numpy as np
import matplotlib.pyplot as plt


sys.path.append(r'D:\code_work\Photonics')      # 添加函数文件位置
import my_library                               # 导入函数文件

t = np.linspace(0,2*np.pi,1000)                  # 时间坐标函数
s = np.sin(5*2*np.pi*t)                          # 正弦函数
plt.figure()                                     # 绘图
plt.plot(t,s)

amp,fre,pha = my_library.my_fft(s, t)           # 调用my_function文件里一个名为my_fft的函数
plt.figure()                                     # 绘图
plt.plot(fre,amp)

plt.show()                                       # 显示绘图
