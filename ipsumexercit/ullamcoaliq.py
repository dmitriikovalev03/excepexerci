import numpy as np

def bound(tempBounds, item, index):
    return np.concatenate((tempBounds, [item]), axis=0)[index]

b = bound(tempBounds, item, 1)
