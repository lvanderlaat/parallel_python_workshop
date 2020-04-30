# Python Standard Library
from os import listdir

# Local files
import spectra
import pymp

datapath = '../data/'

filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']

with pymp.Parallel(2) as p:
    for filename in filenames:
        print('\n\t', filename)
        frequency, amplitude = spectra.compute_FFT(datapath+filename)
        spectra.create_figure(datapath, filename[:-3], frequency, amplitude)
