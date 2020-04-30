print('\n', ' multiprocessing '.center(72, '='))

# Python Standard Library
from os import listdir
from multiprocessing import Pool
from itertools import repeat

# Local files
import spectra

datapath = '../data/'
outpath  = '../out/'

filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']

def calc_plot_spectrum(datapath, filename, outpath):
    print('\n\t', filename)
    frequency, amplitude = spectra.compute_FFT(datapath+filename)
    spectra.create_figure(outpath, filename[:-3], frequency, amplitude)

pool = Pool(2)
pool.starmap(calc_plot_spectrum, zip(repeat(datapath), filenames, repeat(outpath)))
pool.close()
pool.join()
