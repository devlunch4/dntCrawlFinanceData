from pykrx import stock
import json
import pandas as pd


class StockCrawl:
    def __init__(self, start_date, end_date, save_type, save_path):
        self.start_date = start_date
        self.end_date = end_date
        self.save_type = save_type
        self.save_path = save_path

        extension = ['json', 'csv', 'tsv']

        if self.save_type in extension:
            print('Start Stock information Crawl---')
        else:
            print('Check your save file type ---')



    def crawl(self, ticker, ticker_name):
        print(f'stock data lodad----')
        df = stock.get_market_ohlcv_by_date(self.start_date, self.end_date, ticker)
        print(df.tail())
        # df.reset_index(inplace=True, drop=True)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df = df.astype({'open':'str', 'high':'str', 'low':'str',
                        'close':'str', 'volume':'str'})
        print(df.head())

        if self.save_type == 'json':
            self.__to_json(df, ticker, ticker_name, self.save_path)
        elif self.save_type == 'csv':
            self.__to_csv(df, ticker, ticker_name, self.save_path)
        # elif self.save_type == 'tsv':
        #     self.__to_tsv(df, ticker, ticker_name, self.save_path)

    def __to_json(self, df, ticker, ticker_name,save_path):
        if self.save_type == 'json':
            s_dict = {}
            with open(f'{save_path}/{ticker_name}_{ticker}_h.json', 'w') as f:
                for idx, col in df.iterrows():
                    date = idx.strftime('%Y%m%d')
                    s_dict[date] = {}
                    s_dict[date]['open'] = col['open']
                    s_dict[date]['high'] = col['high']
                    s_dict[date]['low'] = col['low']
                    s_dict[date]['close'] = col['close']
                    s_dict[date]['volume'] = col['volume']
                json.dump(s_dict, f, ensure_ascii=False, indent='\t')


    def __to_csv(self, df, ticker, ticker_name, save_path):
        if self.save_type == 'csv':
            df = df.rename_axis('날짜').reset_index()
            df.rename(columns = {'날짜':'date'}, inplace=True)
            df.to_csv(f'{save_path}/{ticker_name}_{ticker}_h.csv', index=False)

    # def __to_tsv(self, df, ticker, ticker_name, save_path):
    #     if self.save_type == 'csv':
    #         df = df.rename_axis('날짜').reset_index()
    #         df.rename(columns = {'날짜':'date'}, inplace=True)
    #         df.to_csv(f'{save_path}/{ticker_name}_{ticker}_h.tsv', index=False, sep='\t')

if __name__ == '__main__':
    stock_eng_name = ['samsung', 'naver']
    stock_code_list = ['005930', '035420']

    start_date = '19990101'
    end_date = '20220301'

    st_crawl = StockCrawl(start_date, end_date, 'csv', './')

    for n,s in zip(stock_eng_name ,stock_code_list):
        s_df = st_crawl.crawl(s, n)




