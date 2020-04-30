from os import rename, system, listdir

datapath = '../data/'
filenames = [filename for filename in listdir(datapath) if filename[-3:] == 'mp3']

for name_mp3 in filenames:
    print(name_mp3)
    new_name_mp3 = name_mp3.replace(' ', '_')
    rename(datapath+name_mp3, datapath+new_name_mp3)
    name_wav = new_name_mp3[:-3] + 'wav'
    system(f'mpg123 -w {datapath+name_wav} {datapath+new_name_mp3}')

