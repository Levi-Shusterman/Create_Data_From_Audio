
def get_song_stats():
    list_song_stats = []
    for x in xrange(1,20):
        song = {}
        song['name'] = 'max'
        song['bpm'] = 4
        song['key'] = 2
        song['notes'] = {'A': 5, 'B': 5}

        x = {}
        x['middle'] = song

        list_song_stats.append(x)

    return list_song_stats

def get_num_of_songs():
    return 20