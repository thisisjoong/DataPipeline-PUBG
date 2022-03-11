import requests

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Berynie"
api_key = ''

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
read_json = r.json()
print(read_json)


matchId = read_json['data'][0]['relationships']['matches']['data'] # 게임 매치 ID

matchId_li = []

for i in range(0,len(matchId)):
  matchId_li.append(matchId[i]['id'])


