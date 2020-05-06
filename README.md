# Basic Parallel Python, an overview

## Python Standard Library

### Example 0: `threading`

`threading` is the Python Standard Library to run shared memory concurrent jobs without the need for a multi-core architecture. Is best suited for I/O, network and database non-CPU-intensive tasks.

`00_freesound_scraping.py` is a simple script to search and download sounds from the [freesound](https://freesound.org/) collaborative database. In `00_freesound_scraping_threading.py`, its multithreaded implementation, we transform the `for` loops to functions definitions, and then initialize a `Thread` object for each queary and sound to download. Measure execution times:

    ./scr/$ time python 00_freesound_scraping.py
    ./scr/$ time python 00_freesound_scraping_threading.py

### Example 1: `multiprocessing`

`multiprocessing` is the Python Standard Library to spawn jobs across a number of CPU's. To know how many parallel processes you can have at any time in your computer do:

    $ python
    >>> from multiprocessing import cpu_count
    >>> cpu_count()

This will print the number of *logical* cores of your computer, not *physical*. 

`10_mp32wav.py` is a script to convert all `mp3` files in a folder to `wav` format. `11_mp32wav_multiprocessing.py` is its parallel version. The `for` loop is transformed to a function definition, then, we create a `Pool` of processes with the available number of cores (`cpu_count`), among which the tasks will be distributed evenly.

To test these scripts, copy a bunch of `mp3` files to the `data` folder, at least ~15 files. Then:

    ./scr/$ time python 10_mp32wav.py
    ./scr/$ time python 11_mp32wav_multiprocessing.py

### Example 2: `multiprocessing`, `pymp` and `mpi4py`

By running the `20_get_spectra.py` script, for each song in `data`, you will sequentially compute a FFT on a 20 s window and then write a `png` file with a simple figure of the resultant spectrum. Measure its execution time:
    
    ./scr/$ time python 20_get_spectra.py

We will paralelize using:

#### `multiprocessing`

We proceed as we did with example 1, creating a `Pool` of processes. In this case, if in OSx this program will most probably crash. There is a conflict with `matplotlib.pyplot` library and the way the processes are spawned or forked in the system, this is a known [bug](https://bugs.python.org/issue33725). 

#### `pymp`

[PyMP](https://github.com/classner/pymp) package brings OpenMP-like functionality to Python, hiding the use of `multiprocessing` library. Using `pymp` package the reference to this problem is printed out once per process, then it continues running sequentially only for the tasks assigned to process 0. Measure the execution time of this script:

    ./scr/$ time python 22_get_spectra_pymp.py

#### `MPI` and `mpi4py`

`MPI`, the Message Passing Interface, is a non-pythonian system, that you can [download](http://www.mpich.org/downloads/) and install in your machine. `mpi4py` is the python library that enable your program to communicate with `MPI`. Both `MPI` and `MPI4Py` are already installed at [Kabré supercomputer](https://kabre.cenat.ac.cr/). Measure the execution time of this script:


    ./scr/$ time mpiexec python 23_get_spectra_MPI.py
