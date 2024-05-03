# importing libraries

#pip3 install requests

import requests
import pandas
import sqlalchemy

url = 'http://api.coincap.io/v2/assets'

header = {'Content-Type':'application/json',
          'Accept-Encoding':'deflate'}

response = requests.get(url,headers=header)

#print(response)

responseData= response.json()

#print(responseData)

df = pandas.json_normalize(responseData,'data')

#print(df.head())

# Connecting SQL to Python
server = 'DESKTOP-73ELNP5'
driver = 'SQL Server Native Client 11.0'
database = 'DataEngineering'

conn_str = f'mssql+pyodbc://@{server}/{database}?driver={driver}'
engine = sqlalchemy.create_engine(conn_str)

#connec = engine.connect()

# Load Data into SQL Server
df.to_sql(name='FactCrypto',con=engine,index=False,if_exists='replace')