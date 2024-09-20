import numpy as np

def filter_applicants(degree,experience ,min_exp,required_degree):
  exp_filter =  experience>= min_exp
  degree_filter = np.isin(degree,required_degree)
  qualified_candidates = exp_filter & degree_filter 
  return qualified_candidates

degree=np.array(["computer sc","mechanical eng","electrical eng "])
experience= np.array([3,2,4])
min_exp= 3
required_degree =["computer sc","electrical eng"]

qualified= filter_applicants(degree,experience,min_exp,required_degree)
print("qualified candidates:",qualified)