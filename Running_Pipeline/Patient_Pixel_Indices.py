import numpy as np

def generate_indices(patient_data_dict):
    indices = []
    for patient_id, patient_data in patient_data_dict.items():
        # Get the number of elements based on the size of the patient_data
        num_elements = len(patient_data)
        # Generate the corresponding indices
        patient_indices = [patient_id] * num_elements
        indices.extend(patient_indices)
    return np.array(indices)