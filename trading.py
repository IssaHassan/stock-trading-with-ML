import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#create the 'target' for the dataset
# assigns value of 1 if a givens day data resulted in the next day
#closing at a higher price
def create_target(data):
    rows = data.shape[0]
    reversed_data = np.flipud(data)
    result = np.zeros(rows)
    first_close = 193.15
    prev = first_close
    i=0
    for x in reversed_data:
        if x[3]>prev:
            result[i]=1
        else:
            result[i]=0
        prev = x[3]
        i=i+1

    return result

#stock price data for Tesla (TSLA)
#identify datatype so each row is interpreted as an element of the  arrayy
#skip first row, and use cols 1toN to avoid the date column
tsla_data = np.loadtxt('tsla.csv', delimiter=",",skiprows=1,usecols=(1,2,3,4,5))

#X_train, X_test, y_train, y_test = train_test_split()
#knn = KNeighborsClassifier(neighbors=3)

target = create_target(tsla_data)

knn = KNeighborsClassifier(n_neighbors=1)
X_train, X_test, y_train, y_test = train_test_split(tsla_data,target,random_state=0)
knn.fit(X_train,y_train)

prediction_set = knn.predict(X_test)
print("Test Score: {}".format(prediction_set))
#print("Test Score: {:.2f}".format(knn.score(X_train,y_train)))
