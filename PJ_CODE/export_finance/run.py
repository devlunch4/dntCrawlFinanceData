import os
from utils.finance_module import ExportFinance

if __name__ == '__main__':
    tickers = {
        'naver': '03420', 'samsung': '005930', 'kakao': '035720'
    }

    if not os.path.exists('output'):
        os.mkdir('output')

    ExportFinance(tickers=tickers, st='19900101', file_type='csv')
    ExportFinance(tickers=tickers, st='19900101', file_type='json')

