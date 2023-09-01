class Parameters():
    '''Container for Qhea parameters'''
    def __init__(self, optimiziation_rate, n_individuals, n_generations, selection_pressure, bias):
        self.optimiziation_rate = optimiziation_rate
        self.n_individuals = n_individuals
        self.n_generations = n_generations
        self.selection_pressure = selection_pressure
        self.bias = bias