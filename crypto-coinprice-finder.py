

import pandas
import json
from binance.client import Client
import requests
f = open('./pairs.json')
data = json.load(f)
i = 0 
api_key = "jfIn2AjrpMuTTmv5cY6uGuq4u08mUqwBYs9i882fiZOFe4s1s0g4fjoSRLKDHu5M"
api_secret = "fmZrmxh5tkmc7qNCJiCK35uOoCHr90D35nYhs1DlY0DgLn0iamZL5uZMrffjwndX"
client = Client(api_key, api_secret)
   


while i < len(data):
    coin_price = client.get_symbol_ticker(symbol=str(data[i]["Portfolio"]))
    # marketcup = requests.get('https://www.binance.com/exchange-api/v2/public/asset-service/product/get-products')
    print(coin_price["price"])
    with open('./pairs.json', "r+") as filewrite:
      file_data = json.load(filewrite)
      file_data[i]["price"] = coin_price["price"]
    #   print("coin price : " + str(coin_price["price"]))
      filewrite.seek(0)
      json.dump(file_data, filewrite, indent = 4)
    with open('./pairs.json', "r+") as filewrite2:
      file_data2 = json.load(filewrite2)
      marketcup = requests.get('https://www.binance.com/exchange-api/v2/public/asset-service/product/get-products')
      datacoin = marketcup.text
      parse_json = json.loads(datacoin)
      z = 0 
      while z < len(parse_json["data"]):
         market_cap = parse_json["data"][z]["s"]
         if market_cap == data[i]["Portfolio"]:
           print(market_cap) 
           print(type(parse_json["data"][z]["cs"]))
           print(type(coin_price["price"]))
           x = int(0 if parse_json["data"][z]["cs"] is None else parse_json["data"][z]["cs"]) * float(coin_price["price"])
           print(x)
           break
         z = z + 1 
      file_data2[i]["marketcap"] = str(x)
      filewrite2.seek(0)
      json.dump(file_data2, filewrite2, indent = 4)

    i = i + 1 
f.close()
