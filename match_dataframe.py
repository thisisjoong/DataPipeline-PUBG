import requests
import pandas as pd
import pprint
import json

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

import matchId

url_match = "https://api.pubg.com/shards/steam/matches/"
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1YzgzYmMwMC1lNjBhLTAxMzktMjZhNi02M2UwOWQxYTU2NmEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjI5NzAwNTg0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImFsbC1hYm91dC1iYXR0In0.WoILL4hA4cJN11gy7pomLFeGNtYdc-1Yv1V-iiK7r9Y'

header = {
  "Authorization": api_key,
  "Accept": "application/vnd.api+json"
}

r = requests.get(url_match+ matchId_li[0], headers=header)
first_match = r.json()
#print(read_json)

first_match_data = first_match['included']  #각 플레이어 관한 데이터가 'attributes'안에 있음
first_match_info = first_match['data']  #해당게임 전반적인 데이터

attribute_li= []

for i in range (len(first_match_data)):
  attribute_li.append(first_match_data[i]['attributes'])


for i in range(len(attribute_li)):
  if 'URL' in attribute_li[i]:
    tele = attribute_li[i]
    print(attribute_li.index(tele))

del attribute_li[67]

stats=[]

for i in range(len(attribute_li)):
  stats.append(attribute_li[i]['stats'])

columns=['name', 'playerId', 'DBNOs', 'assists', 'boosts', 'damageDealt', 'deathType',
         'headshotKills', 'heals', 'killPlace', 'killStreaks', 'kills', 'longestKill',
         'revives', 'rideDistance', 'roadKills', 'swimDistance', 'teamKills', 'timeSurvived',
         'vehicleDestroys', 'walkDistance', 'weaponsAcquired', 'winPlace']

stats_df = pd.DataFrame(stats, columns=columns)


first_match_info['attributes']
match_info_df = pd.DataFrame(first_match_info['attributes'],index=[0])

match_info_df= match_info_df[['mapName', 'createdAt', 'duration', 'gameMode']]

match_info_df

tele_df = pd.DataFrame(data=tele, index=[0])
tele_df = tele_df[['URL']]

# 최종 match_info_df 정리()
match_info_df_result = pd.concat([match_info_df,tele_df], axis=1)
match_info_df_result #0번쨰 경기

# 10경기 채택, first_match(첫경기) 제외
match = []
for i in range(1,len(matchId_li[:10])):
  match.append(requests.get(url_match+ matchId_li[i], headers=header).json())

match_data= []
match_info= []

for i in range(len(match)):
  match_data.append(match[i]['included']) #각 플레이어 관한 데이터가 'attributes'안에 있음(2~10경기 데이터)
  match_info.append(match[i]['data']) #해당게임 전반적인 데이터(2~10 경기 데이터)

match_data[0]  #두번째 경기 included 데이터

len(match_data)  #match_data = [ []*9 ] 형태

#TELEMETRY 정보 제외

for i in range(0, len(match_data[0])):
  if 'URL' in match_data[0][i]['attributes']:
    tele_1 = match_data[0][i]['attributes']
    del_tele_1 = match_data[0][i]
    print(match_data[0].index(del_tele_1))
    print(tele_1)

tele_1

del match_data[0][78]  #두번째 경기 TELE 빼내기

for i in range(0,len(match_data[1])):
  if 'URL' in match_data[1][i]['attributes']:
    tele_2 = match_data[1][i]['attributes']
    del_tele_2 = match_data[1][i]
    print(match_data[1].index(del_tele_2))

for i in range(0,len(match_data[2])):
  if 'URL' in match_data[2][i]['attributes']:
    tele_3 = match_data[2][i]['attributes']
    del_tele_3 = match_data[2][i]
    print(match_data[2].index(del_tele_3))

for i in range(0,len(match_data[3])):
  if 'URL' in match_data[3][i]['attributes']:
    tele_4 = match_data[3][i]['attributes']
    del_tele_4 = match_data[3][i]
    print(match_data[3].index(del_tele_4))

for i in range(0,len(match_data[4])):
  if 'URL' in match_data[4][i]['attributes']:
    tele_5 = match_data[4][i]['attributes']
    del_tele_5 = match_data[4][i]
    print(match_data[4].index(del_tele_5))

for i in range(0,len(match_data[5])):
  if 'URL' in match_data[5][i]['attributes']:
    tele_6 = match_data[5][i]['attributes']
    del_tele_6 = match_data[5][i]
    print(match_data[5].index(del_tele_6))


for i in range(0,len(match_data[6])):
  if 'URL' in match_data[6][i]['attributes']:
    tele_7 = match_data[6][i]['attributes']
    del_tele_7 = match_data[6][i]
    print(match_data[6].index(del_tele_7))

for i in range(0,len(match_data[7])):
  if 'URL' in match_data[7][i]['attributes']:
    tele_8 = match_data[7][i]['attributes']
    del_tele_8 = match_data[7][i]
    print(match_data[7].index(del_tele_8))

for i in range(0,len(match_data[8])):
  if 'URL' in match_data[8][i]['attributes']:
    tele_9 = match_data[8][i]['attributes']
    del_tele_9 = match_data[8][i]
    print(match_data[8].index(del_tele_9))


# 9경기다 url 행 지우기(2번째는 위에서 지웠음)
del match_data[1][63] #63
del match_data[2][70] #70
del match_data[3][71] #71
del match_data[4][33] #33
del match_data[5][19] #19
del match_data[6][16] #16
del match_data[7][79] #79
del match_data[8][58] #58

attributes_2 = []
attributes_3 = []
attributes_4 = []
attributes_5 = []
attributes_6 = []
attributes_7 = []
attributes_8 = []
attributes_9 = []
attributes_10 = []

stats_2 = []
stats_3 = []
stats_4 = []
stats_5 = []
stats_6 = []
stats_7 = []
stats_8 = []
stats_9 = []
stats_10 = []

for i in range(len(match_data[0])):
  attributes_2.append(match_data[0][i]['attributes'])
  stats_2.append(attributes_2[i]['stats'])

for i in range(len(match_data[1])):
  attributes_3.append(match_data[1][i]['attributes'])
  stats_3.append(attributes_3[i]['stats'])

for i in range(len(match_data[2])):
  attributes_4.append(match_data[2][i]['attributes'])
  stats_4.append(attributes_4[i]['stats'])

for i in range(len(match_data[3])):
  attributes_5.append(match_data[3][i]['attributes'])
  stats_5.append(attributes_5[i]['stats'])

for i in range(len(match_data[4])):
  attributes_6.append(match_data[4][i]['attributes'])
  stats_6.append(attributes_6[i]['stats'])

for i in range(len(match_data[5])):
  attributes_7.append(match_data[5][i]['attributes'])
  stats_7.append(attributes_7[i]['stats'])

for i in range(len(match_data[6])):
  attributes_8.append(match_data[6][i]['attributes'])
  stats_8.append(attributes_8[i]['stats'])

for i in range(len(match_data[7])):
  attributes_9.append(match_data[7][i]['attributes'])
  stats_9.append(attributes_9[i]['stats'])

for i in range(len(match_data[8])):
  attributes_10.append(match_data[8][i]['attributes'])
  stats_10.append(attributes_10[i]['stats'])

attributes_2[0]['stats']

matchId_df = pd.DataFrame(data=matchId_li[:10], columns=['matchId'])
matchId_df

#10개의 게임 데이터 추출 코드(stats만 사용하면 됌)

stats_2_df = pd.DataFrame(stats_2, columns=columns)
stats_3_df = pd.DataFrame(stats_3, columns=columns)
stats_4_df = pd.DataFrame(stats_4, columns=columns)
stats_5_df = pd.DataFrame(stats_5, columns=columns)
stats_6_df = pd.DataFrame(stats_6, columns=columns)
stats_7_df = pd.DataFrame(stats_7, columns=columns)
stats_8_df = pd.DataFrame(stats_8, columns=columns)
stats_9_df = pd.DataFrame(stats_9, columns=columns)
stats_10_df = pd.DataFrame(stats_10, columns=columns)

stats_2_df = stats_2_df.dropna()
stats_3_df = stats_3_df.dropna()
stats_4_df = stats_4_df.dropna()
stats_5_df = stats_5_df.dropna()
stats_6_df = stats_6_df.dropna()
stats_7_df = stats_7_df.dropna()
stats_8_df = stats_8_df.dropna()
stats_9_df= stats_9_df.dropna()
stats_10_df= stats_10_df.dropna()

all_match_info = []
for i in range(len(match_info)):
  all_match_info.append(match_info[i]['attributes'])

all_match_info_df = pd.DataFrame(data = all_match_info)

all_match_info_df = all_match_info_df[['createdAt', 'mapName', 'duration', 'gameMode']]


tele_1_df = pd.DataFrame(data=tele_1, index=[0])
tele_1_df = tele_df[['URL']]


all_tele = [tele_1, tele_2, tele_3, tele_4, tele_5, tele_6, tele_7, tele_8, tele_9]

all_tele_df = pd.DataFrame(data=all_tele)

all_tele_df = all_tele_df[['URL']]
all_tele_df = pd.concat([tele_df,all_tele_df], ignore_index=True)


all_match_info_df = pd.concat([match_info_df, all_match_info_df],ignore_index=True)

all_match_info_df = pd.concat([matchId_df, all_match_info_df], axis=1)


# 최종 all_match_info_df (URL이 포함된 형태)

all_match_info_df = pd.concat([all_match_info_df, all_tele_df], axis=1)
# all_match_info_df

# stats(게임 데이터) 데이터프레임에 matchId 추가하기
stats_df = stats_df.dropna()
stats_df.reset_index(drop=True, inplace=True)
stats_2_df.reset_index(drop=True, inplace=True)
stats_3_df.reset_index(drop=True, inplace=True)
stats_4_df.reset_index(drop=True, inplace=True)
stats_5_df.reset_index(drop=True, inplace=True)
stats_6_df.reset_index(drop=True, inplace=True)
stats_7_df.reset_index(drop=True, inplace=True)
stats_8_df.reset_index(drop=True, inplace=True)
stats_9_df.reset_index(drop=True, inplace=True)
stats_10_df.reset_index(drop=True, inplace=True)

from matchId import *
# stats(게임 데이터) 데이터프레임에 matchId 추가하기
stats_df['matchId'] = matchId[0]['id']
stats_2_df['matchId'] = matchId[1]['id']
stats_3_df['matchId'] = matchId[2]['id']
stats_4_df['matchId'] = matchId[3]['id']
stats_5_df['matchId'] = matchId[4]['id']
stats_6_df['matchId'] = matchId[5]['id']
stats_7_df['matchId'] = matchId[6]['id']
stats_8_df['matchId'] = matchId[7]['id']
stats_9_df['matchId'] = matchId[8]['id']
stats_10_df['matchId'] = matchId[9]['id']

