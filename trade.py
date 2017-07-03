import numpy as np
from trading import Model
import v20
import requests

api = v20.Context(
        'api-fxpractice.oanda.com',
        '443',
        token='2f3a1f9ea2bfee5fe9d4c50d9f5ca8c8-c419e02e8c8f0382f897d9c1143ec1a0'
)

account_id = '101-002-6020849-001'

class Trade:

    def __init__(self,fileName):
        self.model = Model(fileName)




    def market_buy(account_id, instr, unitSize):
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

def main():
    instr = ['']
    t = Trade('sp500.csv')
    #t.model.get_score()
    todays_data = np.array([[2431,2439,2428,2429]])
    todays_pred = t.model.predict_next_day(todays_data)[0]
    #if(todays_pred>0) market_buy(account_id,)




if __name__ == "__main__":
    main()
