import math

import numpy as np

__all__ = ['is_valid_solution']


def is_valid_solution(vec):
    m = np.reshape(vec, (int(math.sqrt(len(vec))), int(math.sqrt(len(vec)))))
    sum_cols = np.sum(m, axis=0)
    sum_rows = np.sum(m, axis=1)

    for i in range(len(sum_rows)):
        if sum_rows[i] != 1 or sum_cols[i] != 1:
            return False

    return True



