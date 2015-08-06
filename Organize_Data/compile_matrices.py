# Levi Shusterman
# Israel Tech Challenge Hackathon
from Organize_Data.analyze_parameters import *
from data_from_audio_api import * # Adam's API


class CompileMatrices():

    def __init__(self, filepath):
        # api calls
        self.all_song_data = get_song_stats(filepath)   # a list of dicts
        self.num_of_songs = len(self.all_song_data)  # gets number of songs from first member of list

        # puts matrices together
        self.compile_matrices()

    def compile_matrices(self):
        size = self.num_of_songs
        self.overall_matrix = [[0 for x in range(size)] for x in range(size)]
        self.transition_matrix = [[0 for x in range(size)] for x in range(size)]

        grader = ParamMethods()
        x = 0

        size = self.num_of_songs
        self.overall_matrix = [[0 for x in range(size)] for x in range(size)]
        self.transition_matrix = [[0 for x in range(size)] for x in range(size)]

        grader = ParamMethods()
        x = 0

        while x < size:

            z = 0
            while z < size:

                if x == z:
                    self.transition_matrix[x][z] = -1000
                    self.overall_matrix[x][z] = -1000
                else:
                    self.transition_matrix[x][z] = \
                    grader.grade_parameters(self.all_song_data[x]['end'],
                                            self.all_song_data[z]['begin'])

                z = z+1

            y = x + 1
            while y < size:

                self.overall_matrix[x][y] = \
                grader.grade_parameters( self.all_song_data[x]['middle'],
                                    self.all_song_data[y]['middle'] )
                self.overall_matrix[y][x] = self.overall_matrix[x][y]
                y = y+1
            x = x+1

    def _overall_matrix_give(self):
        return self.overall_matrix

    def _transition_matrix_give(self):
        return self.transition_matrix

    def _aggregate_matrix(self):
        over_matrix = self._overall_matrix_give()
        trans_matrix = self._transition_matrix_give()

        size = self.num_of_songs
        matrix = [[0 for x in range(size)] for x in range(size)]

        for x in range(0, size):
            for y in range(0, size):
                matrix[x][y] = over_matrix[x][y] + trans_matrix[x][y]

        return matrix

    def give_matrix(self):
        return self._aggregate_matrix()
