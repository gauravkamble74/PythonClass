class Cricket:
    def __init__(self, board, country, captain):
        self.board = board
        self.country = country
        self.captain = captain
        print('i am inside constructor')
    
    def teamInfo(self):
        print(f"country of team is {self.country}")
        print(f"board of team is {self.board}")
        print(f"captain of team is {self.captain}")

obj = Cricket("Bcci","India","Virat")
# obj = Cricket()
# obj.board = 'bcci'
obj.teamInfo()
