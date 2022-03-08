from sqlalchemy import create_engine
import pandas as pd
from os import environ

eng = create_engine(environ["SBASE_DB"])
data_lake = pd.read_sql("SELECT * FROM algorand_data", con = eng)

price_data = data_lake.data.values[0]["quote"]["USD"]
payload = (price_data['price'], price_data['last_updated'])

df = pd.DataFrame.from_dict({"price": [price_data['price']], "last_updated": [price_data['last_updated']]})
df.to_sql("algorand_price_data", con = eng, index = False, if_exists = "append")
