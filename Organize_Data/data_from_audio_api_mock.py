
def get_song_stats():
    list_song_stats = []
    for i in xrange(20):
        song = {}
        song['name'] = 'max'
        song['bpm'] = 4
        song['key'] = 2
        song['notes'] = {'A': 5, 'B': 5}

        x = {}
        x['middle'] = song

        list_song_stats.append(song)

def get_num_of_songs():
    return 20