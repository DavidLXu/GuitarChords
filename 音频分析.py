import wave
import numpy
from pyaudio import PyAudio
import matplotlib.pyplot as plt

# 只读方式打开WAV文件
wf = wave.open('./output.wav', 'rb')
# 创建PyAudio对象
p = PyAudio()
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
    channels = wf.getnchannels(),
    rate = wf.getframerate(),
    output = True)
nframes = wf.getnframes()
framerate = wf.getframerate()

# 读取完整的帧数据到str_data中，这是一个string类型的数据
str_data = wf.readframes(nframes)
wf.close()

# 将波形数据转换成数组
wave_data = numpy.fromstring(str_data, dtype=numpy.short)
# 将wave_data数组改为2列，行数自动匹配
wave_data.shape = -1,2
# 将数组转置
wave_data = wave_data.T

def time_plt():
    # time也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标
    time = numpy.arange(0, nframes)*(1.0/framerate)
    # 绘制波形图
    plt.figure()
    plt.subplot(211)
    plt.plot(time, wave_data[0], c='r')
    plt.subplot(212)
    plt.plot(time, wave_data[1], c='g')
    plt.xlabel('time (seconds)')
    # plt.show()

def freq():
    # 采样点数，修改采样点数和起始位置进行不同位置和长度的音频波形分析
    N = 44100
    start = 0  # 开始采样位置
    df = framerate/(N-1)  # 分辨率
    freq = [df*n for n in range(0, N)]  # N个元素
    wave_data2 = wave_data[0][start:start+N]
    c = numpy.fft.fft(wave_data2)*2/N
    # 常规显示采样频率一半的频谱
    d = int(len(c)/2)
    # 仅显示频率在4000以下的频谱
    while freq[d] > 4000:
        d -= 10
    plt.figure()
    plt.plot(freq[:d-1], abs(c[:d-1]), 'r')
    plt.show()

def main():
    time_plt()
    freq()

if __name__ == '__main__':
    main()
