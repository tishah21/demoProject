from flask import Flask,jsonify
from flask_restful import Resource,Api,reqparse
import yfinance as yf
import pandas as pd

tickers = pd.read_html('https://ournifty.com/stock-list-in-nse-fo-futures-and-options.html#:~:text=NSE%20F%26O%20Stock%20List%3A%20%20%20%20SL,%20%201000%20%2052%20more%20rows%20')[0]

final_dict = {}

tickers = tickers.SYMBOL.to_list()

# for ticker in tickers:
#     final_dict[ticker] = ticker+'.NS'

# print(tickers)



app = Flask("VideoAPI")
api = Api(app)


# parser = reqparse.RequestParser()
# parser.add_argument('title',required=True)

class Stocks(Resource):
    def get(self,ticker_symbol):
        if ticker_symbol=="all":
            return tickers
        
        return_obj = {}
        ticker_symbol += '.NS'
        ticker_obj = yf.Ticker(ticker_symbol)
        start_date = "2023-01-01"
        end_date = "2024-01-01"
        stock_data = ticker_obj.history('30y')
        # print(stock_data.columns)
        stock_data.index = pd.to_datetime(stock_data.index, unit='ms')
        stock_data = stock_data.reset_index()

        data_for_analysis = stock_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        return_obj['history'] = data_for_analysis.to_json(orient='records')
        # print(type(ticker_obj.news))
        # return_obj['history'] = ticker_obj.history('30y')
        return_obj['news'] = ticker_obj.news

        return return_obj
        

    

api.add_resource(Stocks,'/stocks/<ticker_symbol>')


if __name__ == '__main__':
    app.run()