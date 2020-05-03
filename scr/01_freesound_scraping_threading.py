import freesound
from threading import Thread

api_key = 'Jx5IEtDs0iD2HjC2Cd0y8BU7pSow2k8h2iW8jbU6'
queries = ['cello', 'harmonica']
data_path = '../freesound_downloads/'

client = freesound.FreesoundClient()
client.set_token(api_key, 'token')

sounds = []

def search(query, sounds):
    print(f'\tQuerying "{query}"')
    results = client.text_search(query=query, fields='id,name,previews')
    for sound in results:
        sounds.append(sound)


def download(sound, data_path):
    print('\t', sound.name)
    sound.retrieve_preview(data_path, sound.name)


threads = []
for query in queries:
    thread = Thread(target=search, args=(query, sounds)) # Shared memory
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for sound in sounds:
    thread = Thread(target=download, args=(sound, data_path))
    thread.start()
