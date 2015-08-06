import sys, csv
from essentia import *
from essentia.standard import *
from pylab import *
from numpy import *

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
    song_stats = {}
    song_stats['bpm'] = bpm
    song_stats['key'] = key + scale_color
    song_stats['notes-used'] = notes
    return song_stats

def analyze_song(filepath):
    song_stats = {}
    song_stats['beginning'] = parse_signal(get_beginning(filepath))
    song_stats['middle'] = parse_signal(get_middle(filepath))
    song_stats['end'] = parse_signal(get_end(filepath))
    print song_stats

"""
# example to get BPM:
audio = MonoLoader(filename ='/Users/adammichaelgross/Desktop/techno_loop.wav')()
bpm_extractor = RhythmExtractor2013()
results = bpm_extractor.compute(audio)
bpm = results[0]
print 'BPM is: ' + str(bpm)

#example to get Key and chords
song = MonoLoader(filename ='/Users/adammichaelgross/Desktop/techno_loop.wav')()
tonal_extractor = TonalExtractor()
results = tonal_extractor(song)
key = results[2]
scale_color = results[5]
notes = results[4]
print 'Key is: ' + str(key) + " " + str(scale_color) + " and notes are:\n " + str(notes)
"""
#print get_beginning('/Users/adammichaelgross/Desktop/techno_loop.wav')
analyze_song('/Users/adammichaelgross/Desktop/techno_loop.wav')
