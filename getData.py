# This script generates historical graph for https://www.cnn.com/markets/fear-and-greed
# If not specified, it will generate the latest one year graph for Fear & Greed Index and its 7 indicators

# Note that historical data are not actively updated. Only need to update every 6 months, since website has latest 10 months data already
import requests, csv, yfinance, pytz, json
from datetime import datetime
def getAllHistoricalData():
    BASE_URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
    START_DATE = '2020-07-14'
    print("Getting data")
    r = requests.get("{}/{}".format(BASE_URL, START_DATE), headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
    print(r)
    data = r.json()
    fg_data = data['fear_and_greed_historical']['data']
    fear_greed_values = {}

    FEAR_GREED_CSV_FILENAME = ['datasets/fear-greed-2020-2023.csv', 'Date,Fear Greed', data['fear_and_greed_historical']['data']]
    MARKET_MOMENTUM = ['datasets/market-momentum-2020-2023.csv', 'Date,Market Momentum', data['market_momentum_sp500']['data']]
    STOCK_PRICE_STRENGTH = ['datasets/stock-price-strength-2020-2023.csv', 'Date,Stock Price Strength',data['stock_price_strength']['data']]
    STOCK_PRICE_BREADTH = ['datasets/stock-price-breadth-2020-2023.csv', 'Date,Stock Price Breadth',data['stock_price_breadth']['data']]
    PUT_AND_CALL_OPTIONS = ['datasets/put-and-call-options-2020-2023.csv', 'Date,Put and Call Options',data['put_call_options']['data']]
    MARKET_VOLATILITY = ['datasets/market-volatility-2020-2023.csv', 'Date,Market Volatility',data['market_volatility_vix']['data']]
    SAFE_HAVEN_DEMAND = ['datasets/safe-haven-demand-2020-2023.csv', 'Date,Safe Haven Demand',data['safe_haven_demand']['data']]
    JUNK_BOND_DEMAND = ['datasets/junk-bond-demand-2020-2023.csv', 'Date,Junk Bond Demand',data['junk_bond_demand']['data']]
    all_Data = [FEAR_GREED_CSV_FILENAME, MARKET_MOMENTUM, STOCK_PRICE_STRENGTH, STOCK_PRICE_BREADTH, PUT_AND_CALL_OPTIONS,
                MARKET_VOLATILITY, SAFE_HAVEN_DEMAND, JUNK_BOND_DEMAND]

    for factor in all_Data:
        with open(factor[0], 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([factor[1]])

            for data in factor[2]:
                dt = datetime.fromtimestamp(data['x'] / 1000, tz=pytz.utc)
                fear_greed_values[dt.date()] = float(data['y'])
                writer.writerow([dt.date(), float(data['y'])])

getAllHistoricalData()