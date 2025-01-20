import os, getpass
import matplotlib.pyplot as plt 
import numpy as np
from os.path import join, getsize


def folder_counter(path):
    path = "dataset//"+path
    return len(next(os.walk(path))[1])

def file_counter(path):
    path = "dataset//"+path
    return len(next(os.walk(path))[2])

def folder_name(path):
    path = "dataset//"+path
    directory_list = list()
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            directory_list.append(name)
    return directory_list

def diagram(path):
    names = folder_name(path)
    counts = {name : 0 for name in names}
    for folder in names:
        path_folder = path +'//' +folder
        counts[folder] = file_counter(path_folder)
    plt.figure()    
    plt.bar(names, counts.values())
    fig, ax = plt.subplots()
    ax.pie(counts.values(), labels=names)
    

def distribution():    
    diagram("./Grape")
    diagram("./Apple")
    plt.show()

distribution()