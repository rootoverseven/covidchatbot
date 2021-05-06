import numpy as np
import matplotlib as plt
from sklearn import datasets, linear_model
dib=datasets.load_diabetes()

print(dib.data[:,np.newaxis,2])