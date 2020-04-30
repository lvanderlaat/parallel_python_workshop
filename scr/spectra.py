from random import randint
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def compute_FFT(filepath):
    rate, data = wavfile.read(filepath)

    # Deal with stereo
    if data.ndim == 2:
        data = data.T
        data = data[0]

    # Trim at random window
    duration = 20
    total_duration = len(data)/rate
    n_samples = duration * rate
    first_sample = randint(1, len(data) - n_samples - 1)
    data = data[first_sample: first_sample+n_samples]

    frequency = np.fft.rfftfreq(len(data), 1/rate)
    amplitude = np.abs(np.fft.rfft(data))
    amplitude /= amplitude.max()
    return frequency, amplitude


def create_figure(outpath, name, frequency, amplitude):
    fig = plt.figure(figsize=(4, 3))
    fig.subplots_adjust(left=.15, bottom=.16, right=.93, top=.89)

    ax = fig.add_subplot(111)
    ax.set_title(name)
    # X axis
    ax.set_xlabel('Frequency [Hz]')
    ax.set_xlim(20, 14000)
    ax.xaxis.set_major_formatter(EngFormatter(unit='Hz'))
    ax.set_xscale('log')
    # Y Axis
    ax.set_ylabel('Normalized amplitude')

    ax.plot(frequency, amplitude, linewidth=1, c='r')
    fig.savefig(outpath+name+'.png', format='png', dpi=200)
    plt.close()
    return
