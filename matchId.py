import requests

url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Berynie"
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1YzgzYmMwMC1lNjBhLTAxMzktMjZhNi02M2UwOWQxYTU2NmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjI5NzAwNTg0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImFsbC1hYm91dC1iYXR0In0.WoILL4hA4cJN11gy7pomLFeGNtYdc-1Yv1V-iiK7r9Y'

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


