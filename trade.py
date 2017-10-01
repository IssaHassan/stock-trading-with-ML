import numpy as np
#from trading import Model
import v20
import requests
# got this from: http://oanda-api-v20.readthedocs.io/en/latest/endpoints/instruments/instrumentlist.html
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import simplejson as json
from model_mlp import Model_MLP
import pandas_datareader as web
import threading
client = oandapyV20.API(access_token='2f3a1f9ea2bfee5fe9d4c50d9f5ca8c8-c419e02e8c8f0382f897d9c1143ec1a0')
account_id = '101-002-6020849-001'
#instr='SPX500_USD'
api = v20.Context(
        'api-fxpractice.oanda.com',
        '443',
        token='2f3a1f9ea2bfee5fe9d4c50d9f5ca8c8-c419e02e8c8f0382f897d9c1143ec1a0'
)

class Trade:
    account_id = '101-002-6020849-001'
    commodity = 'SPX500_USD'
    trade_size = 56 #should change this value based on currr account size.


    def __init__(self, model):
	    self.model = model


    def market_buy(self, account_id, instr, unitSize):
        order_response = api.order.market(
                account_id,
                instrument = instr,
                units=unitSize
        )

        if(order_response.status==201):
                print("Market order has been filled")
        else:
                print("Market order has NOT been filled")

        print(order_response.status)

    def close_order(self,acc_id,instr):
        close_response = api.position.close(
            acc_id,
            instr,
            longUnits = "ALL",
            #shortUnits ='ALL'
        )
        if(close_response.status==200):
            print("Position has been closed")
        else:
            print("Position has NOT been closed")
        print(close_response.status)

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



    def trade(self):
        #goes through the list of trades, once a day. And if there is a
        #commodity that predicts 1, it buys that commodity
        #otherwise it keeps looping.
        threading.Timer(60.0*60, self.trade).start() # called every minute
        #print("Hi")
        next_day = self.get_todays_candle()
        if self.model.predict_next_day(next_day) == 1:
            self.market_buy(self.account_id,self.commodity,self.trade_size)
        else:
            self.close_order(self.account_id,self.commodity)
            #print(self.model.predict_next_day(next_day))






def main():
    mlp = Model_MLP('sp500_hourly2.csv','SPX500_USD')
    t = Trade(mlp)
    t.trade()




if __name__ == "__main__":
    main()
