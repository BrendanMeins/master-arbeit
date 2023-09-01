__all__ = ['Problem', 'TSP']


class Problem(object):
    """
    Container class for information to a benchmark problem
    """

    def __init__(self, name, qubo, minimum, description):
        self.name = name
        self.qubo = qubo
        self.minimum = minimum
        self.description = description


class TSP(object):
    """
    Container for a TSP Distance Matrix
    """

    def __init__(self, name, distances, minimum, description, permutation):
        self.name = name
        self.distances = distances
        self.minimum = minimum
        self.description = description
        self.permutation = permutation
