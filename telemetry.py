import requests
import json
import pprint

#telemetry data
telemetry_url = 'https://telemetry-cdn.pubg.com/bluehole-pubg/steam/2021/09/03/15/37/cf835326-0ccc-11ec-bc41-6eb9a4f2a6c1-telemetry.json'
url = requests.get(telemetry_url)
text = url.text

data = json.loads(text)

pprint.pprint(data, depth=15)
