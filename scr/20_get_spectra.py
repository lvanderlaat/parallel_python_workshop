print('\n', ' Sequential '.center(72, '='))

# Python Standard Library
from os import listdir

# Local files
import spectra

datapath = '../data/'
outpath  = '../out/'

filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']


for filename in filenames:
    print('\n\t', filename)
    frequency, amplitude = spectra.compute_FFT(datapath+filename)
    spectra.create_figure(outpath, filename[:-3], frequency, amplitude)
