import numpy as np
from dwave_qbsolv import QBSolv
import neal
import tsp_qubo

__all__ = ['anneal' , 'tabu']


def anneal(q_mat):
    '''
    :param q_mat: QUBO Matrix to be optimized
    '''
    Q = {
        (i, j): q_mat[i][j] for i in range(len(q_mat)) for j in range(len(q_mat)) if q_mat[i][j] != 0
    }
    
    annealer = neal.SimulatedAnnealingSampler()

    response = annealer.sample_qubo(Q, num_repeats=1)
    vec = np.zeros(len(q_mat))
    r_dict = list(response.samples())[0]
    for key in r_dict:
        vec[key] = r_dict[key]
    return vec.astype(int), response.data_vectors['energy'][0]



def tabu(q_mat):
    '''
    :param q_mat: QUBO Matrix to be optimized
    '''
    Q = {
        (i, j): q_mat[i][j] for i in range(len(q_mat)) for j in range(len(q_mat)) if q_mat[i][j] != 0
    }
    
    response = QBSolv().sample_qubo(Q, num_repeats=1)
    vec = np.zeros(len(q_mat))
    r_dict = list(response.samples())[0]
    for key in r_dict:
        vec[key] = r_dict[key]
    return vec.astype(int), response.data_vectors['energy'][0]
