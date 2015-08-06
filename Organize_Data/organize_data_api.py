from compile_matrices import CompileMatrices

def get_matrix(filepath):
    X = CompileMatrices(filepath)
    return X.overall_matrix_give()

def get_overall_matrix_api(filepath):
    matrix = get_matrix(filepath)

    with open('matrix_file', 'w') as f:
        for row in matrix:
            for value in row:
                f.write(str(value))
                f.write(' ')
            f.write('\n')


