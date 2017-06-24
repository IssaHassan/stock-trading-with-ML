import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#stock price data for Tesla (TSLA)
#identify datatype so each row is interpreted as an element of the  arrayy
#skip first row, and use cols 1toN to avoid the date column
tsla_data = np.loadtxt('tsla.csv', delimiter=",",skiprows=1,usecols=(1,2,3,4,5))
print("First five rows of tesla stock data:\n{}".format(tsla_data[:5]))
