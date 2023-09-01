import numpy as np
import scipy.sparse


class SubProblem():
    

    def __init__(self, q_mat, d_vars_index, f_vars_index) -> None:

        self.d_vars_index = d_vars_index
        self.f_vars_index = f_vars_index

        self.base = self.base(q_mat)
        self.sum_rows_cols = self.sum_rows_cols(q_mat)

    
    def base(self,q_mat) -> np.ndarray:
        base = q_mat[self.d_vars_index]
        base = base.T[self.d_vars_index]
        base = base.T
        return base

    def sum_rows_cols(self, q_mat : np.ndarray) -> np.ndarray:
        frozen_rows = q_mat.T[self.f_vars_index].T[self.d_vars_index]
        frozen_cols = q_mat.T[self.d_vars_index].T[self.f_vars_index].T

        sum_frozen = frozen_rows + frozen_cols

        return sum_frozen  


    def get_qubo(self, x : np.ndarray) -> (np.ndarray, np.ndarray):
        f_vars = x[self.f_vars_index]
        f_obj = self.sum_rows_cols @ f_vars
        sub_qubo = self.base + np.diag(f_obj)

        return sub_qubo, self.d_vars_index

        


class QUBO():
    
    n_vars = 0

    n_sub_problems = 0
    sub_problem_size = 0
    _sub_problems : list[SubProblem] = []



    _sparse_q_mat = None

    


    def __init__(self,q_mat : np.ndarray, sub_problem_size : int) -> None:

        self.n_vars = len(q_mat)
        
        self.n_sub_problems = int(self.n_vars / sub_problem_size)
        self.sub_problem_size = sub_problem_size
        
        self._prepare_sub_problems(q_mat)

        self._sparse_q_mat = scipy.sparse.coo_array(np.triu(q_mat))

    
    def objective_function(self,x) -> float:
        return x @ self._sparse_q_mat @ x
    
    
    def get_sub_problem(self, index) -> SubProblem:
        return self._sub_problems[index]
    

    def _prepare_sub_problems(self, q_mat):
        
        for i in range(self.n_sub_problems):
            d_vars_index = np.arange(i * self.sub_problem_size, i * self.sub_problem_size + self.sub_problem_size)
            f_vars = np.ones(self.n_vars)
            f_vars[d_vars_index] = 0
            f_vars_index = np.where(f_vars == 1)[0]

            sub_problem = SubProblem(q_mat, d_vars_index, f_vars_index)
            self._sub_problems.append(sub_problem) 




    # Method to override
    def derive_original_objective() -> float:
        return None

    

class TSPQUBO(QUBO):

    def __init__(self, d_mat, sub_problem_size: int, penalty : float) -> None:
        self.d_mat = d_mat
        q_mat = self._generate_q_mat(penalty) 
        super().__init__(q_mat, sub_problem_size)

    
    def _generate_q_mat(self, penalty) -> np.ndarray:
        n_nodes = len(self.d_mat)
        constraint_matrix = np.zeros((n_nodes ** 2, n_nodes ** 2))
        dimension = len(constraint_matrix)

        for i in range(dimension):
            for j in range(dimension):

                if i == j:
                    constraint_matrix[i][j] -= 2 * penalty
                else:
                    if int(j / n_nodes) == int(i / n_nodes) or j % n_nodes == i % n_nodes:
                        constraint_matrix[i][j] += 1 * penalty

        
        amp = np.zeros((n_nodes, n_nodes))
        for i in range(len(amp)):
            amp[i][(i + 1) % n_nodes] = 1
        objective = np.kron(amp, self.d_mat)
        q_mat = objective + constraint_matrix
        return q_mat

    



    