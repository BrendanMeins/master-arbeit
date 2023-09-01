import numpy as np
import random

__all__ = ['random_float_between_0_1_uniform', 'random_0_1', 'random_int_range', 'random_sequence_0_1',
           'random_sequence_binary']


def random_float_between_0_1_uniform():
    return random.uniform(0, 1)


def random_0_1():
    r = random.uniform(0, 1)
    return round(r)


def random_int_range(min, max):
    return random.randrange(min, max)


def random_sequence_0_1(length):
    return np.array([random_0_1() for i in range(length)])


def random_sequence_binary(length):
    return np.array([bool(random.getrandbits(1)) for i in range(length)])
