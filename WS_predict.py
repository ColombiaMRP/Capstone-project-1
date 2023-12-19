import requests


url = "http://localhost:9696/WS_train"

house ={'bedrooms':3,
 'bathrooms':4,
 'floors':3,
 'waterfront':0,
 'view':3,
 'condition':2,
 'grade':10,
 'yr_built':2004,
 'lat':47.6846,
 'long':-122.291,
 'sqft_living':1700,
 'sqft_lot':4100,
 'sqft_above':2000,
 'sqft_basement':800,
 'sqft_living15':3200,
 'sqft_lot15':6000}

response = requests.post(url, json=house).json()

print(response)