from .objects import TSP
import os
import json
import tsp_qubo.generate
import numpy as np

__distances = ['distances-10-3-100', 'distances-15-1-100', 'distances-20-1-100', 'distances-30-1-100',
               'distances-50-1-100']

__all__ = ['get_tsp', 'get_tsp_names', 'get_cost_function']


def get_tsp(name) -> TSP:
    """
        Returns a tsp distance instance by name
        :param name: string, name of the tsp to be returned
        :return: problem, benchmark.TSP() class object
        """
    problem_index = __distances.index(name)
    f = open(os.path.join(os.path.dirname(__file__), "distances.json"), "r")
    problems = json.load(f)
    f.close()
    problem = problems[problem_index]
    p = TSP(
        problem['name'],
        problem['distances'],
        problem['minimum'],
        problem['description'],
        problem['permutation'],
    )
    return p


def get_tsp_names():
    return __distances


def get_cost_function(name):
    tsp = get_tsp(name)
    penalty = 1000
    distance_matrix = tsp.distances

    nodes = len(distance_matrix)
    constraint_matrix = np.zeros((nodes ** 2, nodes ** 2))
    constraint_matrix = tsp_qubo.generate.apply_penalties(constraint_matrix, penalty)

    chromosome_size = nodes ** 2

    def cost_function(val):
        c_val = val @ constraint_matrix @ val
        t_mat = np.reshape(val, (nodes, nodes))

        for t in range(nodes):
            c_val += t_mat[t] @ distance_matrix @ t_mat[(t + 1) % nodes]
        return c_val

    return cost_function, chromosome_size
