import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class Trade:

    def __init__(self,fileName):
        #knn,X_test,X_train,y_test,y_train,target,data
        self.data = np.loadtxt(fileName,delimiter=",",skiprows=1,usecols=(1,2,3,4,5))
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.generate_target()

    #generate target data to be used by knn classifier
    def generate_target(self):
        self.target = np.zeros(self.data.shape[0])
        reversed_data = np.flipud(self.data)

        prev = 193.15
        i =0

        for x in reversed_data:
            # x corresponds to each individual tuple in reversed_data,
            #the '3' corresponds to the closing price
            if x[3]>prev:
                self.target[i]=1
            else:
                self.target[i]=0
            prev = x[3]
            i = i+1

        self.target = self.target[::-1]

    def train_model(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data,self.target)
        self.knn.fit(self.X_train,self.y_train)

    def predict_next_day(self,data):
        self.knn.predict(data)

    def get_score(self):
        print("Test Score: {}".format(self.knn.score(self.X_test,self.y_test)))



def main():
    t = Trade('tsla.csv')
    t.train_model()
    t.get_score()

if __name__ == "__main__":
    main()
