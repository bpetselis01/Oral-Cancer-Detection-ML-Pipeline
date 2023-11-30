import numpy as np
from scipy import stats

def remove_outliers_based_on_zscore(data_dict):
    normalized_data_dict = {}  # Initialize a dictionary to store normalized data
    
    user_input = input("Do you want to remove outliers (yes/no): ")
    lowercase_input = user_input.lower()

    if lowercase_input == "no":
        return data_dict
    
    threshold = input("Enter the Std Deviation Threshold: ")

    for patient, features in data_dict.items():
        num_rows, num_cols = features.shape
        normalized_features = np.empty_like(features)
        
        for col in range(num_cols):
            # Calculate the mean and standard deviation for the current feature
            feature_mean = np.mean(features[:, col])
            feature_std = np.std(features[:, col])
            
            # Calculate z-scores for the current feature
            z_scores = np.abs(stats.zscore(features[:, col]))
            
            # Replace the outliers with the feature mean
            is_outlier = z_scores > int(threshold)
            normalized_features[:, col] = np.where(is_outlier, feature_mean, features[:, col])
        
        normalized_data_dict[patient] = normalized_features
    
    return normalized_data_dict