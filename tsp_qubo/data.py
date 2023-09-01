import json
import os

__all__ = ['get_instance_from_json']
def get_instance_from_json(index):
    f = open(os.path.join(os.path.dirname(__file__), "data.json"), "r")
    problems = json.load(f)
    f.close()

    return problems["problems"][index]


def add_instance(instance):
    f = open(os.path.join(os.path.dirname(__file__), "data.json"), "r+")
    data = json.load(f)
    f.seek(0)
    f.truncate()
    print("data")
    print(data)
    data["problems"].append(instance)
    json.dump(data, f)
    f.close()


def data_to_dict(name, tsp, tsp_qubo, minimum_tsp, minimum_tsp_qubo, penalty, distance_from, distance_to):
    dict = {
        "name": name,
        "tsp": tsp,
        "tsp_qubo": tsp_qubo,
        "minimum_tsp": minimum_tsp,
        "minimum_tsp_qubo": minimum_tsp_qubo,

        "parameters": {
            "penalty": penalty,
            "distance": {
                "from": distance_from,
                "to": distance_to
            }
        }
    }
    return dict


