
import numpy as np
import matplotlib.pyplot as plt
import ntpath
import json_db
import os

__all__ = ['plot_evolution', 'plot_n_evolutions']
def plot_evolution(evolution, filename, naming_index):
    db_name = json_db.get_db_name(filename)
  

    json_db.save(db_name, evolution, filename, naming_index )
    plt.plot(evolution)
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.savefig(f'files/{filename}.png')
    plt.show()

def plot_n_evolutions(evolutions, labels, experiment_path):
    head, tail = ntpath.split(experiment_path)
    filename_with_ending = tail or ntpath.basename(head)
    filename_without_ending = filename_with_ending.split('.')[0]
    
    for line in range(len(evolutions)):

        plt.plot(evolutions[line], label=labels[line])
    
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.legend()
    plt.savefig(f'files/{filename_without_ending}.png')
    plt.show()