from compile_matrices import CompileMatrices

def _get_matrix(filepath):
    X = CompileMatrices(filepath)
    return X.give_matrix()

def get_matrix_api(filepath):
    matrix = _get_matrix(filepath)

    with open('matrix_file', 'w') as f:
        for row in matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')

get_matrix_api()