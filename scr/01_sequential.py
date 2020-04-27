print('\n', ' Sequential '.center(72, '='))

# Python Standard Library
from os import listdir

# Local files
from spectra import plot_spectrum


datapath = '../data/'
filepaths = [datapath+filename for filename in listdir(datapath)]

for filepath in filepaths:
    plot_spectrum(filepath)
