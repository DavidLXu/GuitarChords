# 一个和音乐有关的小小项目，送给爱玩吉他的你
# 用电脑麦克听和弦，判断并显示和弦名

# pyaudio录制 -> wave 解析 -> 傅立叶变换解析出音符 -> 使用pychord库组合成和弦名 - >使用fretboard库合成svg图片

# 遇到了vscode 总是当成python2 运行的问题
# 查到的解决方案是 control+shift+P 输入defaultSettings.json 进行设置
# 发现defaultSettings.json 不能直接设置
# defaultSettings.json 是不能直接修改的，只需要添加"code-runner.executorMap.python": "python3 -u"
# 到settings.json就可以了，参考https://github.com/formulahendry/vscode-code-runner/issues/366
# 和 https://blog.csdn.net/lxk234801186/article/details/102905760


# 安装pyaudio又遇到了一些问题，缺一个头文件，参考 https://blog.csdn.net/qq_35425070/article/details/84995691

# 第一步，录音，参见    https://blog.csdn.net/qq_36387683/article/details/91901815
import wave
from pyaudio import PyAudio, paInt16
 
 
CHUNK = 1024 # wav文件是由若干个CHUNK组成的，CHUNK我们就理解成数据包或者数据片段。
FORMAT = paInt16 # 表示我们使用量化位数 16位来进行录音
CHANNELS = 2 #代表的是声道，1是单声道，2是双声道。
RATE = 44100 # 采样率 一秒内对声音信号的采集次数，常用的有8kHz, 16kHz, 32kHz, 48kHz,
                # 11.025kHz, 22.05kHz, 44.1kHz。
RECORD_SECONDS = 6 # 录制时间这里设定了5秒
 
 
def save_wave_file(pa, filename, data):
    '''save the date to the wavfile'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    # wf.setsampwidth(sampwidth)
    wf.setsampwidth(pa.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(data))
    wf.close()
 
 
def get_audio(filepath):
    isstart = str(input("是否开始录音？ （是/否）")) #输出提示文本，input接收一个值,转为str，赋值给aa
    if isstart == str("是"):
        pa = PyAudio()
        stream = pa.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         input=True,
                         frames_per_buffer=CHUNK)
        print("*" * 10, "开始录音：请在5秒内输入语音")
        frames = []  # 定义一个列表
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # 循环，采样率 44100 / 1024 * 5
            data = stream.read(CHUNK)  # 读取chunk个字节 保存到data中
            frames.append(data)  # 向列表frames中添加数据data
        print(frames)
        print("*" * 10, "录音结束\n")
 
        stream.stop_stream()
        stream.close()  # 关闭
        pa.terminate()  # 终结
 
        save_wave_file(pa, filepath, frames)
    elif isstart == str("否"):
        exit()
    else:
        print("无效输入，请重新选择")
        get_audio(filepath)
 
 
def play():
    wf = wave.open(r"01.wav", 'rb')
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=
    wf.getnchannels(), rate=wf.getframerate(), output=True)
 
    # 读数据
    data = wf.readframes(CHUNK)
 
    # 播放流
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
 
    stream.stop_stream() # 暂停播放/录制
    stream.close() # 终止播放
 
    p.terminate() # 终止portaudio会话
 

if __name__ == '__main__':
    filepath = '01.wav'
    get_audio(filepath)
    print('Over!')
    play()


# ctrl K， Ctrl 0 用于折叠全部代码，比较方便
# ctrl K， Ctrl J 用于全部展开
# 第二步，显示波形

