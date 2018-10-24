from nba import careerStats, gatherPlayers, getAllStats

def main():
    
    # getAllStats()

    players = gatherPlayers()
    
    name = input('Enter the full name of the player you want stats on:')

    careerStats(name, players)







if __name__ == "__main__": 
    main()