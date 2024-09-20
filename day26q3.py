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

# Get the first 3 rows of the DataFrame
first_3_rows = df.head(3)

# Display the first 3 rows
print("First 3 rows of the DataFrame:\n", first_3_rows)