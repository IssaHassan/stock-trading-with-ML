from trading import Model
from sklearn.neural_network import MLPClassifier
from datetime import datetime
import numpy as np

import v20
import requests
import oandapyV20
import oandapyV20.endpoints.instruments as instruments

client = oandapyV20.API(access_token='2f3a1f9ea2bfee5fe9d4c50d9f5ca8c8-c419e02e8c8f0382f897d9c1143ec1a0')
account_id = '101-002-6020849-001'
api = v20.Context(
        'api-fxpractice.oanda.com',
        '443',
        token='2f3a1f9ea2bfee5fe9d4c50d9f5ca8c8-c419e02e8c8f0382f897d9c1143ec1a0'
)

class Model_MLP(Model):

    def __init__(self,file_name,instr):
        super(Model_MLP,self).__init__(file_name)
        self.mlp = MLPClassifier(solver='lbfgs', activation='tanh', random_state=0, hidden_layer_sizes=[100,100,100])
        self.instr = instr
        self.train_model()
        self.get_score()
        #self.time_frame = time_frame

    def train_model(self):
        self.mlp.fit(self.X_train,self.y_train)

    def predict_next_day(self,data):
        return self.mlp.predict(data)

    def get_score(self):
        print("Training Score: {:.2f}".format(self.mlp.score(self.X_train,self.y_train)))

        print("Test Score: {:.2f}".format(self.mlp.score(self.X_test,self.y_test)))

    def get_curr_price(self):
        latest_price_time = None
        response = api.pricing.get(
            account_id,
            instruments=self.instr,
            since = latest_price_time,
            includeUnitsAvailable=False

        )

        for price in response.get("prices", 200):
            if latest_price_time is None or price.time > latest_price_time:
                return price.bids[0].price

    def get_todays_candle(self):
        #count is the number of previous candles that we return
        # we need 2, because one represents the previous day, and one represents current time
        #granularity is the time_frame

        today_ohlc = np.zeros(4)

        params = {
            "count": 3,
            "granularity": "H1"
        }

        #the following uses oandapyV20, credit belongs to the creator
        #gets candlestick values such open high low close
        r = instruments.InstrumentsCandles(instrument='SPX500_USD',params=params)
        client.request(r)
        result = r.response['candles'][1]['mid']

        today_ohlc[0]=float(result['o'])/10
        today_ohlc[1]=float(result['h'])/10
        today_ohlc[2]=float(result['l'])/10
        today_ohlc[3]=float(result['c'])/10
        #return r.response
        #print(r.response)
        return today_ohlc.reshape(1,-1)
#use main just for testing.
"""
def main():
    m_mlp = Model_MLP('sp500_hourly2.csv','SPX500_USD')
    #print(m_mlp.get_curr_price())
    #m_mlp.train_model()
    #m_mlp.get_score()
    #print(m_mlp.predict_next_day(m_mlp.X_test[:20]))
    #m_mlp.get_score()
    print(m_mlp.get_todays_candle())

if __name__ == "__main__":
    main()
"""
