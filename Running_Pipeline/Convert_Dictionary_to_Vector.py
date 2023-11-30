import numpy as np

def convert_dict_to_continuous_vector(data_dict, transform_flag=False):
    # Create lists to store individual arrays
    patient_arrays = list(data_dict.values())
    flattened_list = [item for sublist in patient_arrays for item in sublist]

    if transform_flag:
        # Stack the arrays horizontally for a neural network input
        result_vector = np.reshape(flattened_list, (np.shape(flattened_list)[1], np.shape(flattened_list)[0]))
    else:
        # Stack the arrays vertically for an SVM input
        result_vector = np.vstack(flattened_list)

    print(np.shape(result_vector))
    return result_vector