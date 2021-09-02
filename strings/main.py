# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_one = "Ruud Gullit"
player_two = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = player_one + " " + str(goal_0) + ", " + player_two + " " + str(goal_1)
print(scorers)

report = f"{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute"
print(report)

player = "Frank Rijkaard"
first_space = player.find(" ")
first_name = player[:first_space]
print(first_name)

last_name = player[first_space + 1:]
last_name_len = len(last_name)
print(last_name_len)

name_short = first_name[0] + ". " + last_name
print(name_short)

chant = (f"{first_name}! " * len(first_name))[0:-1]
print(chant)

good_chant = (chant[-1] != " ")
print(good_chant)short)

chant = (f"{first_name}! " * len(first_name))
print(chant)

good_chant = (chant[:-1] != " ")
print(good_chant)
