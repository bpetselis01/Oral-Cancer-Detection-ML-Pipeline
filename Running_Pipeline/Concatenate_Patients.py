import numpy as np

def concatenate_raw_data_arrays(array1, array2):
    concatenated_data = np.concatenate([array1, array2], axis=0)
    return concatenated_data