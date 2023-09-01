import numpy as np
from .problem import QUBO
from .parameters import Parameters
from .data import Data

class Qhea():
    fitness = 0 # variable used to index individual for fitness
    value = 1 # variable used to index individual for value, eg. chromosome
    def __init__(self, qubo : QUBO, parameters : Parameters, local_optimizer = None):
        '''
        :param qubo: qubo matrix  to optimize (minimize)
        :param parameters: Parameter oject with params to execute the algorithm
        '''
        self.qubo = qubo # save qubo
        self.local_optimizer = local_optimizer
        self.n_individuals = parameters.n_individuals # size of the population
        self.n_generations = parameters.n_generations # number of generations 
        self.mutation_rate = 0
        self.optimization_rate = parameters.optimiziation_rate # probability of local_optimiztaion
        self.selection_pressure = parameters.selection_pressure
        self.bias = parameters.bias
        self.population = self._init_population()
        self.data = self._init_data() 
        self.probabilities_cumsum =self._init_probabilities_cum_sum() # init data
        
    
    def _init_population(self):
        population = np.array([[0, np.random.randint(0, 2, self.qubo.n_vars)] for j in range(self.n_individuals)],
                      dtype=object) # init population
        
        for ind in range(self.n_individuals):
            population[ind][self.fitness] = self.qubo.objective_function(population[ind][self.value]) # initial fitness to population
        
        population = population[population[:, self.fitness].argsort()] # sort ascending by fitness
        return population


    def _init_data(self):
        execution_data = Data(self.population[0])
        return execution_data
    
    def _init_probabilities_cum_sum(self):
        probabilities = []

        for i in range(1, self.n_individuals+1):
            p = (1 / self.n_individuals) * (self.selection_pressure - (2 * self.selection_pressure - 2) * (
                (i - 1) / (self.n_individuals - 1)))
            probabilities.append(p)
        return np.array(probabilities).cumsum()

   
    
    def local_optimization(self, chromosome):
        r = np.random.uniform(0,1)
        if r < self.optimization_rate:
            order =  np.random.permutation(self.qubo.n_sub_problems)
            for index in order:
                sub_problem = self.qubo.get_sub_problem(index)
                sub_qubo, d_vars_index = sub_problem.get_qubo(chromosome) 
                solution, _ = self.local_optimizer(sub_qubo)
                chromosome[d_vars_index] = solution
        return chromosome

    
    def uniform_crossover_sequence(self):
        probabilities = np.random.uniform(0.0, 1.0, self.qubo.n_vars)

        return probabilities > self.bias
    

    def optimize(self):

        for gen in range(self.n_generations): # evolution loop
            self.mutation_rate = 1 / (gen + 1)
            for ind in range(int(self.n_individuals / 2)):            
                # mutation sequence is an array of [0,1], with a probabilty of mutation_rate for each index to be 1
                mutation_sequence_1 = np.random.random(self.qubo.n_vars) < self.mutation_rate # mutation sequence 1
                mutation_sequence_2 = np.random.random(self.qubo.n_vars) < self.mutation_rate # mutation sequence 2

                # selecting parents probabilistic
                parents = np.array([[0, np.random.randint(0, 2, self.qubo.n_vars)] for j in range(2)],
                      dtype=object)
                
                r = np.random.uniform(0,1)

                index_1 = np.where(self.probabilities_cumsum > r)[0][0]
                parents[0] = self.population[index_1]

                r = np.random.uniform(0,1)
         
                # select parent_2        
                index_2 = np.where(self.probabilities_cumsum > r)[0][0]
                parents[1] = self.population[index_2]
                # mutation sequence is an array of [0,1], with a probabilty of mutation_rate for each index to be 1
                mutation_sequence_1 = np.random.random(self.qubo.n_vars) < self.mutation_rate # mutation sequence 1
                mutation_sequence_2 = np.random.random(self.qubo.n_vars) < self.mutation_rate # mutation sequence 2
                
                crossover_sequence = self.uniform_crossover_sequence()
                # crossover with selected parents (first child), then mutation
                offspring_1_chromosome = np.logical_xor(
                np.add(
                    np.logical_and(parents[0][self.value], crossover_sequence), # getting the genes from first parent (where crossover is 1)
                    np.logical_and(parents[1][self.value], np.logical_not(crossover_sequence)) # getting the genes from second parent (where crossover is 0)
                ),mutation_sequence_1)

                crossover_sequence = self.uniform_crossover_sequence()
                # crossover with selected parents (second child), then mutation
                offspring_2_chromosome = np.logical_xor(
                np.add(
                    np.logical_and(parents[1][self.value], crossover_sequence), # getting the genes from second parent (where crossover is 1)
                    np.logical_and(parents[0][self.value], np.logical_not(crossover_sequence))  # getting the genes from first parent (where crossover is 0)
                ), mutation_sequence_2)
                # note how the order of parents changed for individual 2
                self.population = np.vstack([self.population, np.array([0, offspring_1_chromosome], dtype=object)], dtype=object)
                self.population = np.vstack([self.population, np.array([0, offspring_2_chromosome], dtype=object)], dtype=object)

                if self.local_optimizer != None:
                    offspring_1_chromosome = self.local_optimization(offspring_1_chromosome)
                    offspring_2_chromosome = self.local_optimization(offspring_2_chromosome)
                
                
            # apply fitness to every new individual
            for ind in range(self.n_individuals, len(self.population)):
                self.population[ind][self.fitness] = self.qubo.objective_function(self.population[ind][self.value])
            
            # sort ascending by fitness
            self.population = self.population[self.population[:, self.fitness].argsort()]
            self.population = self.population[:self.n_individuals]
            # add fittest individual to data set
            self.data.add_individual(self.population[0])
        
        # when done, return data set
        return self.data
    