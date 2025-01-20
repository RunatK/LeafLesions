import os
from pathlib import Path

import matplotlib.pyplot as plt

from core.config import PATH_TO_DATASET


def folder_counter(path: str):
    path = str(Path(PATH_TO_DATASET, path))
    return len(next(os.walk(path))[1])


def file_counter(path: str):
    path = str(Path(PATH_TO_DATASET, path))
    return len(next(os.walk(path))[2])


def folder_name(path: str):
    path = str(Path(PATH_TO_DATASET, path))
    directory_list = list()
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            directory_list.append(name)
    return directory_list


def diagram(path: str):
    names = folder_name(path)
    counts = {name : 0 for name in names}
    for folder in names:
        path_folder = str(Path(path, folder))
        counts[folder] = file_counter(path_folder)
    plt.figure()    
    plt.bar(names, counts.values())
    fig, ax = plt.subplots()
    ax.pie(counts.values(), labels=names)
    

def show():    
    diagram("Grape")
    diagram("Apple")
    plt.show()