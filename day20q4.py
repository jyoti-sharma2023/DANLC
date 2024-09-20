import numpy as np 

quantity = np.array([2, 3, 4, 1])
price_per_item = np.array([10.0, 5.0, 8.0, 12.0]) 

Total_cost_of_Items= quantity * price_per_item

total_cost= Total_cost_of_Items.sum()

print("Total_cost_of_Items:",Total_cost_of_Items)
print("total cost:",total_cost)