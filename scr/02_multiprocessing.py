print('\n', ' multiprocessing library '.center(72, '='))

# Python Standard Library
from os import listdir
from multiprocessing import Pool

# Local files
from spectra import plot_spectrum


datapath = '../data/'
filepaths = [datapath+filename for filename in listdir(datapath)]

pool = Pool(min(2, len(filepaths)))
pool.starmap(plot_spectrum, zip(filepaths))
pool.close()
pool.join()
