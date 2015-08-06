# Levi Shusterman
# Israel Tech Challenge Hackathon

import data_from_audio_api # Adam's API
import analyze_parameters

class CompileMatrices(self):

    def __init__(self):
        self.all_song_data = data_from_audio_api.get_song_stats()
        self.num_of_songs = self.data_from_audo_api.get_num_of_songs() # gets number of songs from first member of list

        # puts matrices together
        self.compile_matrices()

    def compile_matrices(self):
        # self.overall_matrix = self.compile_overall_matrix()
        # self.transtion_matrix = self.compile_transition_matrix()
        size = self.num_of_songs
        self.overall_matrix = [[0 for x in range(size)] for x in range(size)]

        x = 0

        while x < size:
            y = x + 1
            while y <= size:

                self.overall_matrix[x][y] = \
                analyze_parameters.overall_analyze_parameters( self.all_song_data[x]['middle'],
                                    self.all_song_data[y]['middle'] )

                y = y+1
            x = x+1



    def compile_overall_matrix(self):


    def compile_transition_matrix(self):



