# Python Standard Library
from os import listdir

# Local files
import spectra

# Other dependencies
import numpy as np
from mpi4py import MPI


datapath = '../data/'

comm    = MPI.COMM_WORLD
size    = comm.Get_size()
my_rank = comm.Get_rank()

if my_rank == 0:
    print('\n', ' MPI '.center(72, '='))
    filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'wav']
else:
    filenames = None
filenames =  comm.bcast(filenames, root=0)

count, res = divmod(len(filenames), size)
counts = [count+1 if rank<res else count for rank in range(size)]
displs = [sum(counts[:rank]) for rank in range(size)]

my_filenames = filenames[displs[my_rank]:displs[my_rank]+counts[my_rank]]

for filename in my_filenames:
    print('\n\t', filename)
    frequency, amplitude = spectra.compute_FFT(datapath+filename)
    spectra.create_figure(datapath, filename[:-3], frequency, amplitude)
