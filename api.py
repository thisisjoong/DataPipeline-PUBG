import requests


#url = "https://api.pubg.com/shards/steam/players/DDEDDE"
url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=Berynie"
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1YzgzYmMwMC1lNjBhLTAxMzktMjZhNi02M2UwOWQxYTU2NmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjI5NzAwNTg0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImFsbC1hYm91dC1iYXR0In0.WoILL4hA4cJN11gy7pomLFeGNtYdc-1Yv1V-iiK7r9Y'

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