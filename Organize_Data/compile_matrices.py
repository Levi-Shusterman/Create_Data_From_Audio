# Levi Shusterman
# Israel Tech Challenge Hackathon

class CompileMatrices():

    def __init__(self):
        import data_from_audio_api_mock # Adam's API
        self.all_song_data = data_from_audio_api_mock.get_song_stats() # a list of dicts
        self.num_of_songs = data_from_audio_api_mock.get_num_of_songs() # gets number of songs from first member of list

        # puts matrices together
        self.compile_matrices()

    def compile_matrices(self):
        import Organize_Data.analyze_parameters

        size = self.num_of_songs
        self.overall_matrix = [[0 for x in range(size)] for x in range(size)]
        grader = Organize_Data.analyze_parameters.ParamMethods()
        x = 0

        while x < size:
            y = x + 1
            while y <= size:

                self.overall_matrix[x][y] = \
                grader.grade_parameters( self.all_song_data[x]['middle'],
                                    self.all_song_data[y]['middle'] )
                y = y+1
            x = x+1
