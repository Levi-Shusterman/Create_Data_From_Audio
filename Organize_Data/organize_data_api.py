from compile_matrices import CompileMatrices

def _get_matrix():
    X = CompileMatrices()
    return X.give_matrix()

def get_matrix_api():
    matrix = _get_matrix()

    with open('matrix.txt', 'w') as f:
        for row in matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')

get_matrix_api()