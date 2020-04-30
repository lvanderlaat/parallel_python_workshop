from os import rename, system, listdir
from multiprocessing import Pool, cpu_count
from itertools import repeat

datapath = '../data/'
filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'mp3']

def pre_process(datapath, name_mp3):
    print(name_mp3)
    new_name_mp3 = name_mp3.replace(' ', '_')
    rename(datapath+name_mp3, datapath+new_name_mp3)
    name_wav = new_name_mp3[:-3] + 'wav'
    system(f'mpg123 -w {datapath+name_wav} {datapath+new_name_mp3}')

pool = Pool(min(cpu_count(), len(filenames)))
pool.starmap(pre_process, zip(repeat(datapath), filenames))
pool.close()
pool.join()
