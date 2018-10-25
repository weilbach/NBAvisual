from nba import careerStats, gatherPlayers, getAllStats
import menu

def main():
    
    # getAllStats()
    menu()

    players = gatherPlayers()
    
    name = input('Enter the full name of the player you want stats on:')

    careerStats(name, players)







if __name__ == "__main__": 
    main()