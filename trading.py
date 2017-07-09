from abc import ABCMeta, abstractmethod
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class Model(metaclass=ABCMeta):

    def __init__(self,fileName):
        #knn,X_test,X_train,y_test,y_train,target,data
        #used rows high-price, low-price, open-price and close-price. Ommiting volume and date.
        self.data = np.loadtxt(fileName,delimiter=",",skiprows=1,usecols=(1,2,3,4))
        self.generate_target()
        #self.target = generate_target2(self.data)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data,
                    self.target,random_state=0)


        #self.knn = KNeighborsClassifier(n_neighbors=8)
        #self.generate_target()
        #self.train_model()

    #generate target data to be used by knn classifier
    def generate_target(self):
        #set size of target array to same number of elements of data matrix
        self.target = np.zeros(self.data.shape[0])
        reversed_data = np.flipud(self.data)
        #this number is only correct for tsla.csv file
        #prev = 193.15
        prev = 1974
        i = 0

        for x in self.data:
            # x corresponds to each individual tuple in reversed_data,
            #the '3' corresponds to the closing price
            if x[3]>prev:
                self.target[i]=1
            else:
                self.target[i]=0
            prev = x[3]
            i = i+1

        #reverse target so they match the data
        #self.target = self.target[::-1]

    def generate_target2(self,stock_data):
        target = np.zeros(stock_data.shape[0])
        prev = 193.15
        i=0

        for x in np.flipud(stock_data):
            if x[3]>prev:
                target[i]=1
            else:
                target[i]
            prev = x[3]
            i=i+1

        return target[::-1]
"""
    @abstractmethod
    def train_model(self):
        # random_state=0 is to give a fixed seed for the pseudorandom generator for
        # getting the same output from the function everytime we run it
        # this means the fixed seed causes the training set and test set to be the
        # same everytime we run the program

        #self.knn.fit(self.X_train,self.y_train)
    @abstractmethod
    def predict_next_day(self,data):
        #return self.knn.predict(data)
    @abstractmethod
    def get_score(self):
    #    print("Training Score: {:.2f}".format(self.knn.score(self.X_train,self.y_train)))

    #    print("Test Score: {:.2f}".format(self.knn.score(self.X_test,self.y_test)))

"""
"""

def main():
    m = Model('sp5002.csv')
    m.train_model()
    m.get_score()

if __name__ == "__main__":
    main()
"""
