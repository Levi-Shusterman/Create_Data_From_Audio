from compile_matrices import CompileMatrices

def get_matrix():
    X = CompileMatrices()
    return X.overall_matrix_give()

def get_overall_matrix_api():
    matrix = get_matrix()

    with open('matrix_file', 'w') as f:
        for row in matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')

get_overall_matrix_api()