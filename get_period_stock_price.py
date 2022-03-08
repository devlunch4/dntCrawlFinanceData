from pykrx import stock


def get_period_stock_price(start_date, end_date, stock_code):
    """
    종목코드에 따른 기간, 날짜별 종가 확인
    :param start_date: 시작 년월일
    :param end_date: 종료 년월일
    :param stock_code: 종목코드
    :return: 날짜 / 시가 / 고가 / 저가 / 종가 / 거래량
    """
    return stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)


# 삼성전자=005930
# 네이버=035420
# 카카오=035720
data = get_period_stock_price('20220101', '20220301', '005930')

print(data)
