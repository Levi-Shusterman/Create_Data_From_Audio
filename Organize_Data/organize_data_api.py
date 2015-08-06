from compile_matrices import CompileMatrices
import sys

def _get_matrix(filepath):
    X = CompileMatrices(filepath)
    return X.give_matrix()

def get_matrix_api(filepath='default'):
    if filepath == 'default':
        filepath = sys.argv[1] 
    matrix = _get_matrix(filepath)

    with open(filepath + 'matrix.txt', 'w') as f:
        for row in matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')

#get_matrix_api()
