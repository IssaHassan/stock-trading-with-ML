from trading import Model
from sklearn.neural_network import MLPClassifier

class Model_MLP(Model):

    def __init__(self,file_name):
        super(Model_MLP,self).__init__(file_name)
        self.mlp = MLPClassifier(solver='lbfgs', random_state=0)

        #self.train_model()

    def train_model(self):
        self.mlp.fit(self.X_train,self.y_train)

    def predict_next_day(self,data):
        self.mlp.predict(data)

    def get_score(self):
        print("Training Score: {:.2f}".format(self.mlp.score(self.X_train,self.y_train)))

        print("Test Score: {:.2f}".format(self.mlp.score(self.X_test,self.y_test)))



def main():
    m_mlp = Model_MLP('sp5002.csv')
    m_mlp.train_model()
    m_mlp.get_score()

if __name__ == "__main__":
    main()
