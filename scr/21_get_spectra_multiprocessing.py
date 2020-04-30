# Python Standard Library
from os import listdir
from multiprocessing import Pool, cpu_count
from itertools import repeat

# Local files
import spectra

datapath = '../data/'

filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']

def calc_plot_spectrum(datapath, filename):
    print('\n\t', filename)
    frequency, amplitude = spectra.compute_FFT(datapath+filename)
    spectra.create_figure(datapath, filename[:-3], frequency, amplitude)

with Pool(cpu_count()) as pool:
    pool = Pool(cpu_count())
    pool.starmap(calc_plot_spectrum, zip(repeat(datapath), filenames))
