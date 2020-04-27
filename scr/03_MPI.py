# Python Standard Library
from os import listdir
from time import time

# Other dependencies
import numpy as np
from mpi4py import MPI

# Local files
from spectra import plot_spectrum


comm    = MPI.COMM_WORLD
size    = comm.Get_size()
my_rank = comm.Get_rank()

if my_rank == 0:
    print('\n', ' MPI '.center(72, '='))
    datapath = '../data/'
    filepaths = [datapath+filename for filename in listdir(datapath)]
else:
    filepaths = None
filepaths =  comm.bcast(filepaths, root=0)

count, res = divmod(len(filepaths), size)
counts = [count+1 if rank<res else count for rank in range(size)]
displs = [sum(counts[:rank]) for rank in range(size)]

my_filepaths = filepaths[displs[my_rank]:displs[my_rank]+counts[my_rank]]

for filepath in my_filepaths:
    plot_spectrum(filepath)
