# Python Standard Library
from os import listdir

# Local files
import spectra
import pymp # multiprocessing por dentro

datapath = '../data/'

filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']

filenames = pymp.shared.list(filenames)

with pymp.Parallel(4) as parallel:
    for index in parallel.range(len(filenames)):
        filename = filenames[index]
        print('\n\t', parallel.thread_num, filename)
        frequency, amplitude = spectra.compute_FFT(datapath+filename)
        spectra.create_figure(datapath, filename[:-3], frequency, amplitude)
