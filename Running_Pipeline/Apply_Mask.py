import numpy as np

def apply_mask(mask_dict, full_feature_dict):
    # Initialize an empty dictionary to store reduced features
    reduced_feature_dict = {}
    
    for patient, mask in mask_dict.items():
        full_feature = full_feature_dict.get(patient, None)
        
        if full_feature is not None:
            # Apply the mask to the full feature array
            reduced_feature = full_feature[np.where(mask == 1)]
            reduced_feature_dict[patient] = reduced_feature
    
    return reduced_feature_dict