import numpy as np
import matplotlib.pyplot as plt

# 设置图形大小
plt.figure(figsize=(10, 8))

# 连续信号：5Hz的正弦波
plt.subplot(2, 1, 1)
t = np.linspace(0, 1, 1000)  # 从0到1秒，1000个点
continuous_signal = np.sin(2 * np.pi * 5 * t)  # 生成正弦波
plt.plot(t, continuous_signal)
plt.title('Continuous Signal: 5Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# 离散信号：单位脉冲序列（在n=0时幅值为1）
plt.subplot(2, 1, 2)
n = np.arange(-5, 6)  # 离散时间点从-5到5
discrete_signal = np.zeros_like(n)
discrete_signal[n == 0] = 1  # 在n=0时设置为1
plt.stem(n, discrete_signal, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Discrete Signal: Unit Impulse Sequence')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# 调整布局并显示图形
plt.tight_layout()
plt.show()