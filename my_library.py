# import other packages
import numpy as np
from scipy.fft import fft

# FFT函数
def my_fft(x,t):
    fft_x = fft(x)                                           #  fft计算
    amp_x = 2*abs(fft_x)/len(x)                              # 纵坐标变换
    label_x = np.linspace(0,int(len(x)/2)-1,int(len(x)/2))   # 生成频率坐标
    amp = amp_x[0:int(len(x)/2)]                             # 选取前半段计算结果即可
    # amp[0] = 0
    fs =1/( t[2]-t[1])                                       # 计算采样频率
    fre = label_x/len(x)*fs                                  # 频率坐标变换
    pha = np.unwrap(np.angle(fft_x))                         # 计算相位角并去除2pi跃变
    return amp,fre,pha                                       # 返回幅度和频率


#  其他函数1

#  其他函数2
