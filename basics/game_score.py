player_name = input("enter player name")
games_played = int(input("enter number of games played: "))
total_score = int(input("enter Total score: "))

average_score = total_score / games_played

print(f"Player: {player_name}\n")
print(f"Games Played: {games_played}\n")
print(f"Total Score: {total_score}\n")
print(f"Average Score: {average_score}")
