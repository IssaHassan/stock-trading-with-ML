from trading import Model
from sklearn.neighbors import KNeighborsClassifier

class Model_KNN(Model):

    def __init__(self,file_name):
        super(Model_KNN,self).__init__(file_name)
        self.knn = KNeighborsClassifier(n_neighbors=6)

    def train_model(self):
        self.knn.fit(self.X_train,self.y_train)

    def predict_next_day(self,data):
        self.knn.predict(data)

    def predict_test(self):
        print(self.knn.predict(self.X_test[:500]))

    def get_score(self):
        print("Training Score: {:.2f}".format(self.knn.score(self.X_train,self.y_train)))

        print("Test Score: {:.2f}".format(self.knn.score(self.X_test,self.y_test)))



def main():
    knn = Model_KNN('sp5002.csv')
    knn.train_model()
    knn.predict_test()
    knn.get_score()


if __name__ == "__main__":
    main()
