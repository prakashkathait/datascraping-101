#connecting to API
#Fetching data and normalize it
#coonnection stablishment to sql
#pushing data to sql conn.

import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://sportapi7.p.rapidapi.com/api/v1/event/xdbsZdb/h2h/events"

headers = {
	"x-rapidapi-key": "04c2b13641mshfa831e7438585cap1a33d8jsn37acad17e0da",
	"x-rapidapi-host": "sportapi7.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
responseData = response.json()

# Normalize the JSON data
df = pd.json_normalize(responseData, 'events')

# Flatten complex columns by converting lists to strings, if any
df = df.apply(lambda col: col.map(lambda x: str(x) if isinstance(x, list) else x))


# Inspect the DataFrame to ensure all data types are compatible with SQL
print(df)

# Optionally, drop any columns that you don't need or that are too complex
df = df.drop(['unnecessary_column'], axis=1)

# Connect to the database
engine = create_engine("mysql+mysqlconnector://root:Prakash24%40@localhost/practice")

# Test the connection and insert the DataFrame into the SQL table
df.to_sql(name='SportsFact1', con=engine, index=False, if_exists='fail')

print("Data inserted successfully.")
