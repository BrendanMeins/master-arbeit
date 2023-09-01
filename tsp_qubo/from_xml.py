import os
import sys
import xml.etree.ElementTree as ET
import numpy as np

problems = {
    "a280.xml": 2579,
    "ali535.xml": 202339,
    "fl1400.xml": 20127,
    "kroA200.xml": 29368,
    "pcb3038.xml": 137694
}

__all__ = []

def get_available_problems() -> list[str]:
    return list(problems.keys())


def get_optimum(name: str):
    return problems.get(name)


def get_problem(file_name: str) -> list[list[float]]:
    root_node = ET.parse(os.path.join(os.path.dirname(__file__), file_name)).getroot()
    vertexes = root_node.findall("graph/vertex")
    matrix = np.array([[float(0) for i in range(len(vertexes))] for j in range(len(vertexes))])

    for i in range(len(vertexes)):
        edges = vertexes[i].findall("edge")
        for j in range(len(edges)):
            node_from = i
            node_to = int(edges[j].text)
            cost = float(edges[j].attrib["cost"])
            matrix[node_from][node_to] = cost

    return matrix


# function takes xml file name as parameter and
# prepares a black box cost function that will
# calculate the penalties on the fly
# cost function will be returned
def get_cost_function(problem, penalty):
    # problem is the tsp distance matrix

    # apply a penalty on the main diagonal axis such that
    # the solving algorithm will be punished if it does "not move"
    # from one node to another
    for i in range(len(problem)):
        problem[i][i] += 2 * penalty

    # cost function declaration
    def cost_function(vec, tsp_distances=problem):
        # the dimension of the corresponding vector is of
        # length len(tsp_distances) ** 2. The dimension of the
        # qubo matrix would be dimension ** 2
        dimension = len(vec)
        fitness = 0
        nodes = len(tsp_distances)
        # iterate over imaginary qubo matrix rows
        for i in range(dimension):
            # iterate over imaginary qubo matrix columns
            for j in range(i,dimension):
                # if i == j, the position is on the main diagonal axis of the imaginary qubo matrix
                # These entries correspond to a value from the distance matrix, such as from node 0 to 1 etc.
                if i == j:
                    # the value of the imaginary qubo matrix is the value from the distance matrix - 2 * the penalty
                    # term, given by the constraints.
                    fitness += (vec[i] * (tsp_distances[int(i / nodes)][i % nodes] - 2 * penalty ) * vec[i])

                # in the case where i != j, there are constrained applied such that rows and cols my only have one
                # entry. That constrained is 1 * the penalty term. If j / node_count == i / node_count,
                # it is the same row. If j % node_count == i % node_count, it is the same column.
                elif int(j / nodes) == int(i / nodes) or j % nodes == i % nodes:
                    fitness += vec[i] * penalty * vec[j] * 2

        # function returns the fitness of the individual
        return fitness

    # function returns the prepared cost function such that it can be used by a solver / ea
    return cost_function
