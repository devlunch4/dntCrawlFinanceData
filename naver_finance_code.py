import pandas as pd
import requests
from urllib import parse
from ast import literal_eval
import datetime


def get_naver_finance(symbol: str, st: str, et: str, freq='week'):
    params = {
        'symbol': symbol,
        'requestType': 1,
        'startTime': st,
        'endTime': et,
        'timeframe': freq
    }
    get_params = parse.urlencode(params)
    url = f'https://api.finance.naver.com/siseJson.naver?{get_params}'
    response = requests.get(url)
    return literal_eval(response.text.strip())


get_finance = get_naver_finance('005930', '0140817', '20220301', 'day')

tmp_df = pd.DataFrame(get_finance[1:], columns=get_finance[0])
