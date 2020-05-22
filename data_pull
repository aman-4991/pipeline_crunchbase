
import csv
import requests
    
url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"
headers = {	
    'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",	
    'x-rapidapi-key': "df8b647b2cmsh81bb0369bb5eed1p1d8a9cjsn39ae7bdb735d"	
    }
querystring = {'pagesize': "40"}
response = requests.request("GET", url, headers=headers, params=querystring).json()

header = response['data']['items'][0]['properties'].keys()

with open('crunchbase.csv', 'a') as f:
    w = csv.DictWriter(f, header)
    for data in response['data']['items']:
        w.writerow(data['properties'])    
