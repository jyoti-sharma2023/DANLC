import pandas as pd
import numpy as np


exam_data = {
    'name': ['RIYA', 'DIYA', 'KAVYA', 'JOY', 'SHIKHA'],
    'score': [12, 9,20,20,17,],
    'attempts': [1, 3, 2, 1, 2,],
    'qualify': ['yes', 'no', 'yes', 'yes', 'yes']
}

# Create the DataFrame
df = pd.DataFrame(exam_data)

# Select the 'name' and 'score' columns
selected_columns = df[['name', 'score']]

# Display the result
print("Selected 'name' and 'score' columns:\n", selected_columns)