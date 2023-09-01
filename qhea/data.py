import numpy as np
class Data():
    '''Container to collect data from the algorithm'''
    fitness = 0
    value = 1
    def __init__(self, individual):
        self.evolution = np.array([individual], dtype=object)
        self.all_time_fittest = individual.copy()

    def add_individual(self, individual):
        self.evolution = np.vstack([self.evolution, individual])
        if self.all_time_fittest[self.fitness] > individual[self.fitness]:
            self.all_time_fittest = individual.copy()

    def get_evolution(self):
        return self.evolution
    
    def get_fitness_evolution(self):
        return self.evolution[:, self.fitness]
    
    def get_individual_evolution(self):
        return self.evolution[:, self.value]
    
    def get_solution(self):
        return self.all_time_fittest