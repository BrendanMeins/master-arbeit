import math

import numpy as np
from util import rand, generate
from tsp_qubo import solver, data

__all__ = ['random_tsp', 'random_tsp_qubo']


def generate_and_save(name, nodes, min_val, max_val, penalty):
    tsp = random_tsp(nodes, min_val, max_val, penalty)
    tsp_qubo = random_tsp_qubo(tsp, penalty)

    qubo_min, tsp_min = solver.find_minimum_qubo_and_tsp(tsp_qubo, tsp)

    problem = data.data_to_dict(name=name,
                                tsp=tsp.tolist(),
                                tsp_qubo=tsp_qubo.tolist(),
                                minimum_tsp=tsp_min,
                                minimum_tsp_qubo=qubo_min,
                                penalty=int(penalty),
                                distance_from=int(min_val),
                                distance_to=int(max_val))

    data.add_instance(instance=problem)


# generate random tsp distances
def random_tsp(nodes, min_val, max_val, penalty):
    matrix = generate.generate_matrix(nodes)

    for i in range(nodes):
        for j in range(i, nodes):
            if i != j:
                r = rand.random_int_range(min_val, max_val)
                matrix[i][j] += r
                matrix[j][i] += r

    return matrix


# generate a random tsp qubo matrix with applied penalties
def random_tsp_qubo(tsp, penalty):
    nodes = len(tsp)

    dimension = nodes ** 2

    qubo_matrix = generate.generate_matrix(int(dimension))

    qubo_matrix = apply_distances(qubo_matrix, tsp)

    qubo_matrix = apply_penalties(qubo_matrix, penalty)

    return qubo_matrix


def apply_distances(qubo_matrix, distances):
    dimension = len(qubo_matrix)
    nodes = int(math.sqrt(dimension))

    for i in range(dimension):
        qubo_matrix[i][i] += distances[int(i / nodes)][i % nodes]

    return qubo_matrix


def apply_penalties(qubo_matrix, penalty):
    dimension = len(qubo_matrix)
    nodes = math.sqrt(dimension)
    for i in range(dimension):
        for j in range(dimension):

            if i == j:
                qubo_matrix[i][j] -= 2 * penalty
            else:
                if int(j / nodes) == int(i / nodes) or j % nodes == i % nodes:
                    qubo_matrix[i][j] += 1 * penalty

    return qubo_matrix
