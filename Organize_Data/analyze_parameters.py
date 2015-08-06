
# Class that is meant to evaluate parameters and return a grade
# for two song data that are passed to it
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

        return grade / num_of_params # return the average

    # assign a function to grade two parameters based on the name of the dict key
    # this is meant to allow us to change the parameters that we use flexibly
    def _assign_function(self, key_from_dict):
        if key_from_dict in 'grade_genre':
            return self._grade_genre
        elif key_from_dict in 'grade_key':
            return self._grade_key
        elif key_from_dict in 'grade_bpm':
            return self._grade_bpm

    def _grade_genre(self):
        return 1
    def _grade_key(self):
        return 1
    def _grade_bpm(self):
        return 1
