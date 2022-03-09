import datetime
import logging
import sys
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from os import environ
import pandas as pd
from sqlalchemy import create_engine

def get_exchange_data():

  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': environ["COIN_MKT_CAP"],
  }

  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {'start':'1', 'limit':'50', 'convert':'USD'}
  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params = parameters)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  alg_data = [x for x in data["data"] if x["id"] == 4030 and x["symbol"] == "ALGO"][0]
  payload = pd.DataFrame.from_dict({"data": [json.dumps(alg_data)]})
  
  return(payload)

if __name__ == '__main__':

  df = get_exchange_data()
  eng = create_engine(environ["SBASE_DB"])
  df.to_sql("algorand_data", con = eng, index = False, if_exists = "append")
