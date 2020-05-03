# Python Standard Library
from os import listdir
from multiprocessing import Pool, current_process
from itertools import repeat

# Local files
import spectra

datapath = '../data/'

filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']

def calc_plot_spectrum(datapath, filename):
    print('\n\t', current_process()._identity[0], filename)
    frequency, amplitude = spectra.compute_FFT(datapath+filename)
    spectra.create_figure(datapath, filename[:-3], frequency, amplitude)

with Pool() as pool:
    pool.starmap(calc_plot_spectrum, zip(repeat(datapath), filenames))
