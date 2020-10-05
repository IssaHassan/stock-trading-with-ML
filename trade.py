import numpy as np
from trading import Model
import v20
import requests
# got this from: http://oanda-api-v20.readthedocs.io/en/latest/endpoints/instruments/instrumentlist.html
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import simplejson as json
from model_mlp import Model_MLP
import pandas_datareader as web
import threading
client = oandapyV20.API(access_token='c0dc1d24fed3f9278c5f5fe7151faa53-b022edabd5f826ef9bbe4c1b4eb3f57a')

api = v20.Context(
        'api-fxpractice.oanda.com',
        '443',
        token='c0dc1d24fed3f9278c5f5fe7151faa53-b022edabd5f826ef9bbe4c1b4eb3f57a'
)

class Trade:
    account_id = '101-002-16669501-001'
    commodity = 'SPX500_USD'
    trade_size = 18 #should change this value based on currr account size.


    def __init__(self, model):
        #self.model = Model(fileName)
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


    def trade(self):
        #goes through the list of trades, once a day. And if there is a
        #commodity that predicts 1, it buys that commodity
        #otherwise it keeps looping.
        threading.Timer(60.0*60, self.trade).start() # called every minute
        #print("Hi")
        next_day = self.model.get_todays_candle()
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
