from classes.player import Player

players = [Player("Dana"), Player("Avi"), Player("Noa")]
players[0].add_points(50)
players[1].add_points(15)
players[2].add_points(40)


leader = max(players, key=lambda p: p.points)
print("Leader:", leader)
