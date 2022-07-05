import requests
import json

url = 'https://www.virustotal.com/vtapi/v2/url/report'
girilen_url = input("url: ")

params = {'apikey':'<api key>','resource':girilen_url}

response = requests.get(url,params=params)
json_response = json.loads(response.text)

for item in json_response['scans']:
    print(item, " : ",json_response["scans"][item]['result'])
