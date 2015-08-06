# Levi Shusterman
# Israel Tech Challenge Hackathon
from Organize_Data.analyze_parameters import *
from data_from_audio_api_mock import * # Adam's API


class CompileMatrices():

    def __init__(self):
        self.all_song_data = get_song_stats() # a list of dicts
        self.num_of_songs = get_num_of_songs() # gets number of songs from first member of list

        # puts matrices together
        self.compile_matrices()

    def compile_matrices(self):
        size = self.num_of_songs
        self.overall_matrix = [[0 for x in range(size)] for x in range(size)]
        grader = ParamMethods()
        x = 0

        while x < size:
            y = x + 1
            while y < size:

                self.overall_matrix[x][y] = \
                grader.grade_parameters( self.all_song_data[x]['middle'],
                                    self.all_song_data[y]['middle'] )
                y = y+1
            x = x+1
        print 2

def test():
    X = CompileMatrices()
    X.compile_matrices()
test()