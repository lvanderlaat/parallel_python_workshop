import freesound


api_key = 'Jx5IEtDs0iD2HjC2Cd0y8BU7pSow2k8h2iW8jbU6'
queries = ['cello', 'harmonica']
data_path = '../freesound_downloads/'

client = freesound.FreesoundClient()
client.set_token(api_key, 'token')

sounds = []

for query in queries:
    print(f'\tQuerying "{query}"')
    results = client.text_search(query=query, fields='id,name,previews')
    for sound in results:
        sounds.append(sound)


for sound in sounds:
    print('\t', sound.name)
    sound.retrieve_preview(data_path, sound.name)


