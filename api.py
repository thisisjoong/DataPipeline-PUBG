import requests


#url = "https://api.pubg.com/shards/steam/players/DDEDDE"
url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Berynie"
api_key = ''

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
read_json = r.json()
#print(read_json)


print(read_json['data'][0]['id'])
# id - account.840d28236c3b4bd2aba9b1e2baa92ef0

# matchId = read_json['data'][0]['relationships']['matches']['data']

# for i in range(0,len(matchId)):
#   print(matchId[i]['id'])
