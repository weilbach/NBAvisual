import requests
import json

url = 'http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2017-18&TeamID=1610612756'
url2 = 'http://stats.nba.com/stats/commonallplayers/?LeagueID=00&Season=2017-18&IsOnlyCurrentSeason=1'
url3 = 'http://stats.nba.com/stats/scoreboard/?GameDate=02/14/2015&LeagueID=00&DayOffset=0'
request_headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'stats.nba.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
#get all players
response=requests.get(url2, headers = request_headers)
# print (response.text)
#get player stats
data = response.json()
for player in data:
    print(player)
    if player == 'resultSets':
        for result in player:
            print(result)

    print('\n')