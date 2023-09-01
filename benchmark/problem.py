from .objects import Problem
import os
import json
import numpy as np

__all__ = ['get_instance', 'get_names']

problem_names = ['random-30', 'tsp-5-25-10-20', 'tsp-5-25-10-100', 'tsp-5-25-1-5']


def get_instance(name) -> Problem:
    """
    Returns a problem instance by name
    :param name: string, name of the problem to be returned
    :return: problem, benchmark.Problem() class object
    """
    problem_index = problem_names.index(name)
    f = open(os.path.join(os.path.dirname(__file__), "problems.json"), "r")
    problems = json.load(f)
    f.close()
    problem = problems[problem_index]
    p = Problem(
        problem['name'],
        problem['qubo'],
        problem['minimum'],
        problem['description']
    )

    return p


def get_names():
    return problem_names
