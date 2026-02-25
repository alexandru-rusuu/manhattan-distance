from scipy.spatial.distance import cityblock


def manhattan_manual(X, Y):
    if len(X) != len(Y):
        raise ValueError("Vectorii trebuie sa aiba aceeasi dimensiune")
    
    return sum(abs(x - y) for x, y in zip(X, Y))


def manhattan_scipy(X, Y):
    return cityblock(X, Y)


def parse_vector_from_line(line):
    return list(map(float, line.strip().split()))
