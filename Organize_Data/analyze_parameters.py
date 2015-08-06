
def analyze_parameters(**kwargs):
    #iterate through kwargs and
    grader = ParamMethods()

    for key, value in kwargs.iteritems():
        param_to_grade = grader.assign_function(key)

class ParamMethods(object):

    def __init__(self, genre = 1, key = 1, bpm = 1):
        self.genre_weight = genre
        self.key_weight = key
        self.bpm_weight = bpm

    def assign_function(self, key_from_dict, value):
        if key_from_dict in 'grade_genre':
            return grade_genre
        pass

    def grade_genre(self):
        pass

    def grade_key(self):
        pass

    def grade_bpm(self):
        pass
