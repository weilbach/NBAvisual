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

# def gatherPlayers():
    #turn a lot of stuff into better stuff
data = response.json()
unfinishedRows = data['resultSets']
finishedRows = unfinishedRows[0]
rowSets = finishedRows['rowSet']

players = []


for people in rowSets:

    players.append({
        'playerId' : people[0],
        'playerName' : people[2]
    })
# print (players)
# return players

# def getAllStats(players):
url = 'http://stats.nba.com/stats/commonplayerinfo/?PlayerID='

playerURL = url + '202325' #number for test
finalURL = playerURL + url3
response = requests.get(playerURL, headers = request_headers)
# toPrint = response.json()
print(response)


def careerStats():
    #use either 'Totals' or 'PerGame' for PerMode parameter
    url2 = 'http://stats.nba.com/stats/playercareerstats/?PlayerID='
    ulr3 = 'PerMode=Totals'

'http://stats.nba.com/stats/playercareerstats/?PlayerID=202325&PerMode=Totals'