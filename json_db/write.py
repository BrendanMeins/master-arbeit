import os
import json
import numpy as np


__all__ = ['save']
def save(db_name : str, data : np.ndarray, name, naming_index : int ):
    
    data = data.tolist()
    label = name.split('_')
    if len(label)< naming_index:
        naming_index = 0
    label = label[-naming_index : len(label)]
    final_label = ""
    for i in range(len(label)):
        label[i][0].upper()
        if i == len(label) - 1:
            final_label += label[i]
        else:
            final_label += f'{label[i]} '
 

    obj = {
        'evolutions' : data,
        'label' : final_label
    }
    
    obj = json.dumps(obj)
    with open(f'{db_name}', "w") as outfile:
        outfile.write(obj)
