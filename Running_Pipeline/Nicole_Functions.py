import numpy as np
import os
import matplotlib.pyplot as plt
import math
from scipy.io import loadmat

def convert_data_to_dict(data_labels):
    data_dict = {}
    
    mat_file_path = input("Filepath to Directory with MATLAB Files: ")
    mat_file_name = input("Common Regex for Files to Include: ")
    mat_file_parameter = input("Name of Key Associated to Raw Data: ")

    for label in data_labels:
        file_path = os.path.join(mat_file_path, f"{label}{mat_file_name}.mat")
        mat_file = loadmat(file_path)
        feature = mat_file[mat_file_parameter]

        # Extract xsize, ysize, and zsize
        xsize, ysize, zsize = feature.shape
        data_dict[label] = feature.reshape((xsize * ysize, zsize))

    return data_dict

# Example usage:
# mat_file_path = "/Users/Nicol/OneDrive/Desktop/Nicole_UNSW/VIP 2023/Features - Qatar/"
# mat_file_name = "_LESION_full_feature"
# data_labels = ["Q3", "Q8", "Q12", "Q15", "Q17", "Q22", "Q24", "Q26", "Q28", "Q29", "Q30", "Q31", "Q32", "Q33", "Q36", "Q39", "Q41", "Q44", "Q45", "Q47", "Q48", "Q51", "Q53", "Q55", "Q57", "Q58", "Q61", "Q64", "Q68"]
# mat_file_parameter = "full_feature"

# Convert the MATLAB mask into appropriate dictionary with patient labels
def convert_mask_to_dict(mask_labels):
    mask_dict = {}
    
    mat_file_path = input("Filepath to Directory with MATLAB Files: ")
    mat_file_name = input("Common Regex for Files to Include: ")
    mat_file_parameter = input("Name of Key Associated to Raw Data: ")

    for label in mask_labels:
        file_path = os.path.join(mat_file_path, f"{label}{mat_file_name}.mat")
        mat_file = loadmat(file_path)
        mask = mat_file[mat_file_parameter]

        # Assuming mask is a 1D array with appropriate data
        mask_dict[label] = mask.flatten()

    return mask_dict


def normalize(data_dict):
    min_val = np.inf
    max_val = -np.inf
    
    user_input = input("Do you want to normalize (yes/no): ")
    lowercase_input = user_input.lower()

    if lowercase_input == "no":
        return data_dict
    
    # Find the global minimum and maximum values across all arrays
    for key, value in data_dict.items():
        local_min = np.min(value, axis=0)
        local_max = np.max(value, axis=0)
        min_val = np.minimum(local_min, min_val)
        max_val = np.maximum(local_max, max_val)
    
    normalized_dict = {}
    
    # Normalize each array using the global minimum and maximum values
    for key, value in data_dict.items():
        normalized = (value - min_val) / (max_val - min_val)
        normalized_dict[key] = normalized
    
    return normalized_dict

# Example usage:
# cancer_data_dict = normalize(cancer_data_dict)


def randomize_labels(labels):
    return np.random.permutation(labels)

# Example usage:
# randomized_labels = randomize_labels(data_labels)
# print(randomized_labels)


# Function to split labels into groups based on a percentage
# Example: [1,2,3,4,5,6,7,8,9,10] and 0.3 percent will give [[1,2,3],[4,5,6],[7,8,9,10]]
def split_labels(labels, percentage):
    num_elements = math.floor(percentage * len(labels))
    num_rows = math.floor(len(labels) / num_elements)

    # Create a dictionary to store sets of labels
    divided_labels = {}
    
    for i in range(1, num_rows + 1):
        start_index = (i - 1) * num_elements
        end_index = min(i * num_elements, len(labels))
        set_of_labels = labels[start_index:end_index]

        # Store the set in the dictionary with the row index as the key
        divided_labels[i] = set_of_labels

    # Handle the leftover labels
    leftover_index = num_elements * num_rows
    divided_labels[num_rows + 1] = labels[leftover_index:]

    return divided_labels

# Example usage:
# splitted_labels = split_labels(randomized_labels, 0.2)


def select_labels(split_labels):
    # Assuming you want to select the first group
    first_entry = list(split_labels.items())[0]
    first_value = first_entry[1]
    return first_value

# Example usage:
# selected_labels = select_labels(splitted_labels)
# print(selected_labels)


# Function to get testing data based on selected labels
# testing data will be popped off data_dict
def get_testing_data(data_dict, selected_labels, transpose):
    testing_data = {}
    
    if transpose == "yes":
        transpose == True
    else:
        transpose == False
    
    for key in selected_labels:
        data = data_dict.pop(key)
        testing_data[key] = data.T if transpose else data
    
    return testing_data, data_dict

# Example usage:
# testing_data, cancer_data_dict = get_testing_data(cancer_data_dict, selected_labels, False)
# for data in testing_data:
#     print(f"Size of testing data: {data.shape}")


# Function to get training data from the remaining data in data_dict
def get_training_data(data_dict, transpose):
    training_data = {}
    
    if transpose == "yes":
        transpose == True
    else:
        transpose == False
    
    # Create a copy of the keys to avoid dictionary size changes during iteration
    keys_to_remove = list(data_dict.keys())
    
    for key in keys_to_remove:
        data = data_dict.pop(key)
        training_data[key] = data.T if transpose else data
    
    return training_data

# Example usage:
# training_data = get_training_data(cancer_data_dict, False)
# for data in training_data:
#     print(f"Size of training data: {data.shape}")