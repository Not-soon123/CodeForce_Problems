Number_Of_Game = int(input())
Score = input()

Anton_Score = Score.count("A")
Danic_Score = Number_Of_Game - Anton_Score
if Anton_Score > Danic_Score:
    print("Anton")
elif Danic_Score > Anton_Score:
    print("Danik")
else:
    print("Friendship")