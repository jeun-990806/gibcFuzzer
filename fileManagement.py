import os
import pickle
import sys
sys.setrecursionlimit(10000)


def saveData(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)
    f.close()


def openData(path):
    if os.path.isfile(path) and os.path.getsize(path) > 0:
        with open(path, 'rb') as f:
            result = pickle.load(f)
        f.close()
    else:
        if path.endswith('.dict'):
            result = {}
        if path.endswith('.list'):
            result = []
    return result
