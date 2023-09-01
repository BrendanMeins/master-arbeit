import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
parent = os.path.dirname(parent)


sys.path.append(parent)

import numpy as np
import plotter
import json_db
import papermill as pm
from pathlib import Path
import matplotlib.pyplot as plt


all_db_names = json_db.get_all_dbs_in_dir(__file__)

print(all_db_names)

evolutions = np.array([[] for i in range(len(all_db_names))])
labels = np.array([])

evolutions = [json_db.load(all_db_names[i])['evolutions'] for i in range(len(all_db_names))]

for i in range(len(all_db_names)):
    data = json_db.load(all_db_names[i])
    labels = np.append(labels, data['label'])

for line in range(len(evolutions)):

        plt.plot(evolutions[line], label=labels[line])
    
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.savefig(os.path.abspath('') + 'sum.png')
plt.show()



