#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n):
#Do you have an Instagram account? (y/n): y

#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

print("SURVEY")
quetion1 = input("Are you interested in computer science? (y/n)")
quetion2 = input("Do you like playing computer games? (y/n): ")
quetion3 = input("Do you have an Instagram account? (y/n): ")
print("SURVEY RESULTS")
if quetion1 == "y":
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")
if quetion2 == "y":
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")
if quetion3 == "y":
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")