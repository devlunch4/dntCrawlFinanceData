from pykrx import stock
import json


def save_json(input_stock_code, input_json_string, input_path):
    """
    종목 코드에 따른 data json 파일 저장

    :param input_stock_code: 종목 코드-파일명 설정값
    :param input_json_string: string 화 된 json
    :param input_path: 저장 경로
    :return: None
    """
    input_json_string = json.loads(str(input_json_string))
    # SAVE KOREAN SETTING encoding='UTF-8-sig'
    file = open(input_path + input_stock_code + '_W.json', "w", encoding='UTF-8-sig')
    # SAVE KOREAN dump SETTING ensure_ascii=False
    json.dump(input_json_string, file, ensure_ascii=False)
    file.close()
    print(input_stock_code, ': END save json')


def save_csv(input_stock_code, input_data, input_path):
    """
    종목 코드에 따른 data csv 파일 저장

    :param input_stock_code:
    :param input_data:
    :param input_path:
    :return:
    """
    input_data.to_csv(input_path + input_stock_code + '_W.csv')
    print(input_stock_code, ': END save csv')


def data_replace_string(input_data):
    """
    종목 코드에 따른 입력 데이터 내 unicode 한글 변경(replAce) 및 날짜 표기 변경(iso) 후 output_string 출력

    :param input_data: 종목 코드에 의한 data
    :return: output_string
    """
    output_string = input_data.to_json(orient='columns', date_format='iso')
    output_string = str(output_string).replace('\\ub0a0\\uc9dc', 'date').replace('\\uc2dc\\uac00', '시가') \
        .replace('\\uace0\\uac00', '고가').replace('\\uc800\\uac00', '저가') \
        .replace('\\uc885\\uac00', '종가').replace('\\uac70\\ub798\\ub7c9', '거래량')
    return output_string


def get_period_stock_price(input_stock_code, input_start_date, input_end_date):
    """
    종목 코드에 따른 기간, 날짜별 종가 확인

    :param input_stock_code: 설정 종목 코드
    :param input_start_date: 시작 년월일
    :param input_end_date: 종료 년월일
    :return: data[날짜 / 시가 / 고가 / 저가 / 종가 / 거래량]
    """
    return stock.get_market_ohlcv_by_date(input_start_date, input_end_date, input_stock_code)


if __name__ == '__main__':
    stock_code = '005930'  # 삼성전자 = '005930'
    # stock_code = '035420'  # 네이버 = '035420'
    # stock_code = '035720'  # 카카오 = '035720'

    stock_code_list = {'005930', '035420', '035720'}

    start_date = '19990101'
    end_date = '20220301'

    for stock_code in stock_code_list:
        data = get_period_stock_price(stock_code, start_date, end_date)

        save_json(stock_code, data_replace_string(data), './data/')
        save_csv(stock_code, data, './data/')
        print('>>>', stock_code, 'json, csv END')
