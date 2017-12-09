import os
import numpy as np
import pandas as pd
from pomegranate import *

labelpath = os.path.join('./data/smaller.csv')
X = np.array(pd.read_csv(labelpath))
X_train = X[24000]
X_test = X[6000]
model = BayesianNetwork.from_samples(X_train, algorithm='exact')
print('hi')