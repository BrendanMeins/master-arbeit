import ntpath
import glob
import numpy as np
__all__ = ['get_db_name', 'get_all_dbs_in_dir']

def get_db_name(filname : str):
    json_db_name = filname + '.json'
    return json_db_name

def get_all_dbs_in_dir(path : str):
    head, tail = ntpath.split(path)
    filename_with_ending = tail or ntpath.basename(head)
    dir_path = path.replace(filename_with_ending, '*.json')
    
    abs_paths = glob.glob(dir_path)
    names = np.array([])

    for i in range(len(abs_paths)):
        names = np.append(names, ntpath.basename(abs_paths[i]).split('.')[0] + ".json")

    return abs_paths

    