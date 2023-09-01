import numpy as np
import json
import os

__all__ = ['load']
def load(file_path):
    with open(file_path, 'r') as openfile:

        json_object = json.load(openfile)
 
    return json_object
