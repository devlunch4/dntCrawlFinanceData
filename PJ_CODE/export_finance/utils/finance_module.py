import json
import datetime
from pykrx import stock
from collections import OrderedDict


class ExportFinance:
    def __init__(self, tickers, st, ed=None, file_type='csv'):
        """
        :param tickers: 종목코드 - 지원타입 dict, list, str
        :param st: 시작 시간
        :param ed: 끝나는 시간 None 시 오늘 날
        :param file_type: csv, json파일만 지원
        """
        self.st = st
        if ed is None:
            self.ed = datetime.datetime.now().strftime("%Y%m%d")
        else:
            self.ed = ed
        self.file_type = file_type.lower()

        if file_type is None:
            raise 'You must set a Type. Support csv, json'
        elif (file_type != 'csv') and (file_type != 'json'):
            raise 'Support only csv, json. Check your extentions'

        if isinstance(tickers, dict):
            for idx, ticker in tickers.items():
                self.get_period_stock_price(ticker)

        elif isinstance(tickers, list):
            for ticker in tickers:
                self.get_period_stock_price(ticker)

        elif isinstance(tickers, str):
            self.get_period_stock_price(tickers)

    def get_period_stock_price(self, ticker):

        stock_data = stock.get_market_ohlcv_by_date(self.st, self.ed, ticker)
        stock_data.reset_index(inplace=True)
        stock_data.rename(columns={'날짜': 'Date', '시가': 'Open', '고가': 'High', '저가': 'Low',
                                   '종가': 'Close', '거래량': 'Trading'}, inplace=True)

        self.export_data(stock_data, ticker)

    def export_data(self, data, ticker):
        if self.file_type == 'json':
            stock_dict = OrderedDict()
            with open(f'./output/{ticker}_P.json', 'w') as f:
                for _, values in data.iterrows():
                    date = values['Date'].strftime('%Y%m%d')
                    stock_dict[date] = {}
                    stock_dict[date]['Open'] = values['Open']
                    stock_dict[date]['High'] = values['High']
                    stock_dict[date]['Low'] = values['Low']
                    stock_dict[date]['Close'] = values['Close']
                    stock_dict[date]['Trading'] = values['Trading']

                json.dump(stock_dict, f, ensure_ascii=False, indent='\t')

        elif self.file_type == 'csv':
            data.to_csv(f'./output/{ticker}_P.csv', index=False)
