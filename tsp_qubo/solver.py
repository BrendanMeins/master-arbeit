import math

import tsp_qubo.validate
import util.generate
import numpy as np

__all__ = ['resolve_tsp', 'find_minimum_qubo_and_tsp']


def find_minimum_qubo_and_tsp(qubo, tsp):
    end = False
    a = util.generate.generate_array(len(qubo))

    minimum_qubo_matrix = {
        "vector": [],
        "minimum": float("inf")
    }
    minimum_tsp_matrix = {
        "vector": [],
        "minimum": float("inf")
    }
    while not end:
        a, end = increment(a)

        if tsp_qubo.validate.is_valid_solution(a):

            result_qubo = np.sum(np.multiply(np.outer(a, a), qubo))
            result_tsp = resolve_tsp(a, tsp)

            if result_qubo < minimum_qubo_matrix["minimum"]:
                minimum_qubo_matrix["minimum"] = int(result_qubo)
                minimum_qubo_matrix["vector"] = a.tolist()

            if result_tsp < minimum_tsp_matrix["minimum"]:
                minimum_tsp_matrix["minimum"] = int(result_tsp)
                minimum_tsp_matrix["vector"] = a.tolist()

    return minimum_qubo_matrix, minimum_tsp_matrix


def resolve_tsp(vec, tsp):
    m = np.reshape(vec, (int(math.sqrt(len(vec))), int(math.sqrt(len(vec)))))

    r = np.sum(np.multiply(m, tsp))

    return r


def increment(vec):
    for i in range(len(vec) - 1, 0, -1):
        vec[i] = vec[i] ^ 1

        if vec[i] == 1:
            return vec, False

    return vec, True


def find_minimum_for_cost_function(cost_function, dimension):
    end = False
    a = np.array([0 for i in range(dimension)])
    fitness = float("Inf")
    best_vec = []
    while not end:
        a, end = increment(a)

        if tsp_qubo.validate.is_valid_solution(a):
            result = cost_function(a)
            if result < fitness:
                fitness = result
                best_vec = a.copy()

    return fitness, best_vec
