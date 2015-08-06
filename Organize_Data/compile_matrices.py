# Levi Shusterman
# Israel Tech Challenge Hackathon

import data_from_audio_api_mock # Adam's API
import analyze_parameters

class CompileMatrices(self):

    def __init__(self):
        self.all_song_data = data_from_audio_api_mock.get_song_stats() # a list of dicts
        self.num_of_songs = self.data_from_audio_api_mock.get_num_of_songs() # gets number of songs from first member of list

        # puts matrices together
        self.compile_matrices()

    def compile_matrices(self):

        from analyze_parameters import ParamMethods

        size = self.num_of_songs
        self.overall_matrix = [[0 for x in range(size)] for x in range(size)]
        grader = analyze_parameters.ParamMethods()
        x = 0

        while x < size:
            y = x + 1
            while y <= size:

                self.overall_matrix[x][y] = \
                ParamMethods.grade_parameters( self.all_song_data[x]['middle'],
                                    self.all_song_data[y]['middle'] )
                y = y+1
            x = x+1

