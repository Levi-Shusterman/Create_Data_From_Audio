import sys, csv
from essentia import *
from essentia.standard import *
from pylab import *
from numpy import *


def parse_input_file(filepath):
    song_list = []
    with open(filepath) as file:
        for line in file:
            song_list.append(line)
    song_list.remove(0)
    return song_list


def get_name(filepath):
    front = str.rfind(filepath, '/')
    end = str.find(filepath, '.wav')
    return filepath[front+1:end]


def get_beginning(filepath):
    audio = MonoLoader(filename =filepath)()
    duration_finder = Duration()
    duration = duration_finder(audio)
    return EasyLoader(filename =filepath, startTime=duration*.1, endTime=duration*.15)()


def get_middle(filepath):
    audio = MonoLoader(filename =filepath)()
    duration_finder = Duration()
    duration = duration_finder(audio)
    return EasyLoader(filename =filepath, startTime=duration*.4, endTime=duration*.45)()


def get_end(filepath):
    audio = MonoLoader(filename =filepath)()
    duration_finder = Duration()
    duration = duration_finder(audio)
    return EasyLoader(filename =filepath, startTime=duration*.7, endTime=duration*.75)()


def parse_signal(audio):
    bpm_extractor = RhythmExtractor2013()
    bpm = bpm_extractor.compute(audio)[0]

    tonal_extractor = TonalExtractor()
    results = tonal_extractor(audio)
    key = results[2]
    scale_color = results[5]
    notes = results[4]
    
    note_count = {}
    for note in notes:
        if note not in note_count:
            print('here')
            note_count[note] = 1
        else:
            print('there')
            note_count[note] += 1

    song_stats = {}
    song_stats['bpm'] = bpm
    song_stats['key'] = key + scale_color
    song_stats['notes-used'] = note_count
    
    return song_stats

def analyze_song(filepath):
    song_stats = {}
    song_stats['name'] = get_name(filepath)
    song_stats['beginning'] = parse_signal(get_beginning(filepath))
    song_stats['middle'] = parse_signal(get_middle(filepath))
    song_stats['end'] = parse_signal(get_end(filepath))
    print song_stats
    return song_stats


if '__name__' == '__main__':
    filepath = sys.argv[1]
    song_list = parse_input_file(filepath)
    song_stats = []
    for song in song_list:
        song_stats.append(analyze_song(song))
    return song_stats
        

#analyze_song('/Users/adammichaelgross/Desktop/techno_loop.wav')
