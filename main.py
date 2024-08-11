import requests
import pandas as pd
url = "https://sportapi7.p.rapidapi.com/api/v1/event/xdbsZdb/h2h/events"

headers = {
	"x-rapidapi-key": "04c2b13641mshfa831e7438585cap1a33d8jsn37acad17e0da",
	"x-rapidapi-host": "sportapi7.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
responseData = response.json()
# print(responseData) #to inspect the content in api
# print(response.json())
df = pd.json_normalize(responseData,'events')
print(df)