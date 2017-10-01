class StockData:
	
	__filename = 'sp500_hourly2.csv'
	
	def __init__(self):

		#input rows (1-4) high, low, open and close prices and omit rows 0,5,6
        self.data = np.loadtxt(fileName,delimiter=",",skiprows=1,usecols=(1,2,3,4))
        #print(self.data[:5])
        self.target = self.generate_target2(self.data)
        
		#split data into training and test
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data,
                    self.target,random_state=0)
	
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