# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_One = "Ruud Gullit"
player_Two = "Marco van Basten"
goal_0 = "35"
goal_1 = "54"

scores = player_One + str(goal_0) + "," + player_Two + str(goal_1)
print(scores)

report = player_One + f" scored in the {goal_0}nd minute\n" + player_Two + f" scored in the {goal_1}th minute"
print(report)

player = "Frank Rijkaard"
first_name = player[:player.find(" ")]
print(first_name)

last_name = player[player.find(" ") + 1:]
last_name_len = len(last_name)
print(last_name_len)

name_short = first_name[0] + ". " + last_name
print(name_short)

chant = (f"{first_name}! " * len(first_name))
print(chant)

good_chant = (chant[:-1] != " ")
print(good_chant)
