import pandas as pd
import numpy as np

def create_target_array(patient_data_dict, is_patient_cancerous):
    target_array = np.array([])

    for patient, data_array in patient_data_dict.items():

        # Append 1 if cancerous, 0 if not
        target_array = np.concatenate([target_array, np.ones(data_array.shape[0], dtype=int)]) if is_patient_cancerous else np.concatenate([target_array, np.zeros(data_array.shape[0], dtype=int)])
        # Append True if cancerous, False if not
        # target_array = np.concatenate([target_array, np.full(data_array.shape[0], is_patient_cancerous, dtype=bool)])
    
    return target_array