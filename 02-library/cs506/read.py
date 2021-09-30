def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    f = open(csv_file_path, 'r')
    lines = f.readlines()
    f.close()

    matrix = []

    for line in lines:
        processed_line = line[:-1].split(',') #ignore newline and split by commas
        matrix.append(processed_line)

    return matrix
