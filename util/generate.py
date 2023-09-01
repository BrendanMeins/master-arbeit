import random

import numpy as np

__all__ = ['generate_matrix', 'generate_array', 'generate_array_of_type', 'generate_array_binary']


def generate_matrix(dimension):
    return np.array([[0 for i in range(dimension)] for j in range(dimension)])


def generate_array(length):
    return np.array([0 for i in range(length)])


def generate_array_of_type(data_type, length):
    return np.array([data_type for i in range(length)])


def generate_array_binary(length):
    return np.array([bool(random.getrandbits(1)) for i in range(length)])


