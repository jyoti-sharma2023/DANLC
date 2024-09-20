import pandas as pd
import numpy as np


exam_data = {
    'name': ['RIYA', 'DIYA', 'KAVYA', 'JOY', 'SHIKHA'],
    'score': [12, 9,20,20,17,],
    'attempts': [1, 3, 2, 1, 2,],
    'qualify': ['yes', 'no', 'yes', 'yes', 'yes']
}

# Define index labels
index_labels = ['student1', 'student2', 'student3', 'student4', 'student5']

# Create the DataFrame
df = pd.DataFrame(exam_data, index=index_labels)

# Display the DataFrame
print("DataFrame:\n", df)
