""" This module provides functions to plot a spectrum of a random window of
    data from music wav file """

# Python Standard Library
from os import path
from random import randint

# Other dependencies
import numpy as np
from scipy.io import wavfile
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter


def plot_spectrum(filepath, duration=60, show=False, outpath='../out/'):

    name = path.split(filepath)[1].split('.')[0]

    frequency, amplitude = compute_FFT(filepath, duration)

    # write_figure(name, frequency, amplitude, show=show)

    return


def compute_FFT(filepath, duration):
    # Load
    rate, data = wavfile.read(filepath)

    # Trim at random window
    total_duration = len(data)/rate
    n_samples = duration * rate
    first_sample = randint(1, len(data) - n_samples - 1)
    data = data[first_sample: first_sample+n_samples]

    # Spectrum
    frequency = np.fft.rfftfreq(len(data), 1/rate)
    amplitude = np.abs(np.fft.rfft(data))
    amplitude = savgol_filter(amplitude, 111, 1)
    amplitude /= amplitude.max()
    return frequency, amplitude


def write_figure(name, frequency, amplitude, show=True):
    fig = plt.figure(figsize=(4, 3))
    fig.subplots_adjust(left=.15, bottom=.16, right=.93, top=.89)

    ax = fig.add_subplot(111)
    ax.set_title(name)
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Normalized amplitude')
    ax.plot(frequency, amplitude, linewidth=.5)
    ax.set_xlim(20, 16000)
    ax.set_xscale('log')
    ax.xaxis.set_major_formatter(EngFormatter(unit='Hz'))
    if show:
        plt.show()
    else:
        fig.savefig(f'../out/{name}.png', format='png', dpi=300)
    return


