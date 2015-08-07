
# Class that is meant to evaluate parameters and return a grade
# for two song data that are passed to it
import math

class ParamMethods(object):

    def __init__(self, note =.5 , key = 1, bpm = 2):
        # we can override these later based on our research
        # these constructor variables must add up to a whole number
        # that is equal to how many they are
        self.note_weight = note
        self.key_weight = key
        self.bpm_weight = bpm
        self.num_of_params = self.note_weight+self.key_weight+self.bpm_weight

    # Returns a grade for a transition betweeen two songs
    def grade_parameters( self, first_song, second_song):
    # iterate through kwargs and give a grade based on each parameter, take the average
        grade = 0.0
        self.song_one = first_song
        self.song_two = second_song

        # compare two songs
        for (key, value) in first_song.iteritems():
            if key in second_song:
                value2 = second_song[key]
                # analyze the parameter
                param_func_grade = self._assign_function(key) # which parameter to analyze?
                grade += param_func_grade(self.song_one, self.song_two) # grade the overlap, of two things, such as bpm
                        # grade the overlap, of two things, such as bpm
            else:
                print "%s ; inconsistent keys received\n" % (key)
        
        return (grade/self.num_of_params) # return the average

    # assign a function to grade two parameters based on the name of the dict key
    # this is meant to allow us to change the parameters that we use flexibly
    def _assign_function(self, key_from_dict):
        if key_from_dict in 'notes':
            return self._grade_notes
        elif key_from_dict in 'key':
            return self._grade_key
        elif key_from_dict in 'bpm':
            return self._grade_bpm
        else:
            return self._zero_func

    def _grade_notes(self, song1, song2):
        notes1 = song1['notes']
        notes2 = song2['notes']
        score = 0
        bigger = {}
        smaller = {}
        if len(notes1) > len(notes2):
            bigger = notes1
            smaller = notes2
        else:
            bigger = notes2
            smaller = notes1

        for note in bigger:
            if note in smaller:
                score += 3
            else:
                score -= 3
        return self.note_weight * (50 + score)

    def _grade_key(self, song1, song2):
        key1 = song1['key']
        key2 = song2['key']
    
        circle_of_fifths = {'C': 0, 'Am' : 0,
                        'G' : 1, 'Em': 1, 
                        'D' : 2, 'Bm': 2, 
                        'A' : 3, 'F#m': 3, 'Gbm' : 3,
                        'E' : 4, 'C#m': 4, 'Dbm' : 4,
                        'B' : 5, 'G#m' : 5, 'Abm' : 5, 
                        'Gb' : 6, 'Ebm': 6, 'F#' : 6,
                        'Db': -5, 'Bbm': -5, 'C#' : -5,
                        'Ab' : -4, 'Fm' : -4, 'G#' : -4,
                        'Eb' : -3, 'Cm' : -3, 'D#' : -3,
                        'Bb' : -2, 'Gm' : -2, 'A#' : -2,
                        'F' : -1, 'Dm': -1}
        
        val1 = circle_of_fifths[key1]
        val2 = circle_of_fifths[key2]
        dif = abs(val1 - val2)
        if dif > 6:
            dif = 6 - dif % 6
        
        return self.key_weight*(99 - 15 * dif)

    def _grade_bpm(self, song1, song2):
        bpm1 = song1['bpm']
        bpm2 = song2['bpm']
        normalized1 = bpm1/100
        normalized2 = bpm2/100
        return self.bpm_weight*(99 - abs(normalized1 - normalized2))
    
    def _zero_func(self):
        return 0
