
# Class that is meant to evaluate parameters and return a grade
# for two song data that are passed to it
import math

class ParamMethods(object):

    def __init__(self, genre = 1, key = 1, bpm = 1):
        # we can override these later based on our research
        # these constructor variables must add up to a whole number
        # that is equal to how many they are
        self.genre_weight = genre
        self.key_weight = key
        self.bpm_weight = bpm

    # Returns a grade for a transition betweeen two songs
    def grade_parameters( self, first_song, second_song):
    # iterate through kwargs and give a grade based on each parameter, take the average
        grade = 0.0
        num_of_params = 0.0

        # compare two songs
        for (key, value), (key2, value2) in first_song.iteritems(), second_song.iteritems():
            if key == key2:
                # analyze the parameter
                param_func_grade = self.assign_function(key) # which parameter to analyze?
                grade += param_func_grade(value, value2) # grade the overlap, of two things, such as bpm
            else:
                print "%s != %s ; incorrect keys received\n" % (key, key2)
            num_of_params += 1

        return (grade/num_of_params) # return the average

    # assign a function to grade two parameters based on the name of the dict key
    # this is meant to allow us to change the parameters that we use flexibly
    def _assign_function(self, key_from_dict):
        if key_from_dict in 'genre':
            return self._grade_notes
        elif key_from_dict in 'key':
            return self._grade_key
        elif key_from_dict in 'bpm':
            return self._grade_bpm
        else:
            return self._zero_func

    
    
    circle_of_fifths = {'C': 0, 'Am' : 0,
                        'G' : 1, 'Em': 1, 
                        'D' : 2, 'Bm': 2, 
                        'A' : 3, 'F#m': 3, 'Gbm' : 3,
                        'E' : 4, 'C#m': 4, 'Dbm' : 4,
                        'B' : 5, 'G#m' : 5, 'Abm' : 5, 
                        'Gb' : 6, 'Ebm', 6, 'F#' : 6,
                        'Db': -5, 'Bbm': -5, 'C#' : -5,
                        'Ab' : -4, 'Fm' : -4, 'G#' : -4,
                        'Eb' : -3, 'Cm' : -3, 'D#' : -3,
                        'Bb' : -2, 'Gm' : -2, 'A#' : -2,
                        'F' : -1, 'Dm': -1}
    
    
    def _grade_notes(self, notes1, notes2):
        score = 0
        if self.song1['key'] == self.song2['key']
            return 99
        else:
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
                    score += 1
                else:
                    score -= 1
        return 50 + score

    def _grade_key(self, key1, key2):
        val1 = circle_of_fifths[key1]
        val2 = circle_of_fifths[key2]
        dif = abs(val1 - val2)
        if dif > 6:
            dif = 6 - dif % 6
        
        return 99 - 10 * dif

    def _grade_bpm(self, bpm1, bpm2):
        normalized1 = bpm1/100
        normalized2 = bpm2/100
        return 99 - abs(normalized1 - normalized2)
    
    def _zero_func(self):
        return 0
