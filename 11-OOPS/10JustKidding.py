class Cricket:
    def __init__(myself, board, country, captain):
        myself.board = board
        myself.country = country
        myself.captain = captain
        print('i am inside constructor')
    
    def teamInfo(myself):
        print(f"country of team is {myself.country}")
        print(f"board of team is {myself.board}")
        print(f"captain of team is {myself.captain}")

obj = Cricket("Bcci","India","Virat")

obj.teamInfo()

