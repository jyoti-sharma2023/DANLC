import numpy as np 

inventory = np.array([10, 0, 5, 0, 20, 0]) 

Out_of_Stock_Products= np.where(inventory ==0)[0]
print("_of_Stock_Products:",Out_of_Stock_Products)