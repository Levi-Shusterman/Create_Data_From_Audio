from compile_matrices import CompileMatrices

def _get_matrix():
    X = CompileMatrices()
    return X.overall_matrix_give(), X.transition_matrix_give()

def get_matrix_api():
    matrix, trans_matrix = _get_matrix()

    with open('matrix.txt', 'w') as f:
        for row in matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')

        f.write('\n')

        for row in trans_matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')

get_matrix_api()