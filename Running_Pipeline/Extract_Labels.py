import pandas as pd

def extract_labels():
    # UI: Upload the file (Applies to both Full Feature & Mask)
    file_path = input("Filepath: ")
    df = pd.read_excel(file_path)
    
    # UI: Column Names Found, Please Choose which Dataset to use
    column_names = [col for col in df.columns if not col.startswith('Unnamed')]
    print("Detected Column Names (Datasets):", ', '.join(column_names))
    input_dataset = input("Choose Dataset: ")
    chosen_dataset = df[input_dataset]
    
    # UI: Ask for names of two classes
    positive = input("Positive Class: ")
    negative = input("Negative Class: ")
    
    # UI: Please enter all labels belonging to the positive class (Including the Label of the Positive Class)
    prompt = "Enter Subclasses of " + positive + ": "
    positive_subclasses = []
    done = False
    while (not done):
        string = input(prompt)
        positive_subclasses.append(string)
        if (string == ""):
            done = True
    
    # UI: Please enter all labels belonging to the negative class (Including the Label of the Negative Class)
    prompt = "Enter Subclasses of " + negative + ": "
    negative_subclasses = []
    done = False
    while (not done):
        string = input(prompt)
        negative_subclasses.append(string)
        if (string == ""):
            done = True
            
    # UI: User enters the "categories" of different Diagnoses that the Database has, has the option of grouping labels
    filtered_pos = [item for item in positive_subclasses if item != '']
    filtered_neg = [item for item in negative_subclasses if item != '']
    labels = {}

    # Assign 'positive_data_labels' to positive subclasses
    for subclass in filtered_pos:
        labels[subclass] = 'positive_data_labels'

    # Assign 'negative_data_labels' to negative subclass
    for subclass in filtered_neg:
        labels[subclass] = 'negative_data_labels'

    print(labels)
    
    # UI: Processing your request, creating sets of data
    positive_data_labels = []
    negative_data_labels = []
    for index, condition in enumerate(chosen_dataset):
        if condition in labels:
            label = labels[condition]
            locals()[label].append(f'Q{index + 1}')
            
    print(f"Positive Patients: {positive_data_labels}")
    print(f"Negative Patients: {negative_data_labels}")
    
    return positive_data_labels, negative_data_labels