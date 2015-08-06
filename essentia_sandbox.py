import sys, csv
from essentia import *
from essentia.standard import *
from pylab import *
from numpy import *


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


