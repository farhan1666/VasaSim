import random
rapid_acc = 0.7247 #Accuracy and max hit of rapid with no rigour
rapid_max = 59
rapid_rigour_acc = 0.7673 #Accuracy and max hit of rapid with rigour
rapid_rigour_max = 72
accurate_rigour_acc = 0.7722 #Accuracy and max hit of accurate with rigour
accurate_rigour_max = 74
number_of_players = 2 #Number of players in the raid
teleportedIn = int(number_of_players / 2)
if number_of_players % 2 != 0:
	teleportedIn = teleportedIn + 1

def applyVeng(number_of_players, teleportedIn):
	totalDamage = 121 * teleportedIn
	damage_per_person = int(totalDamage / number_of_players)
	recoiled_damage = number_of_players * int(damage_per_person * 0.75) + int(damage_per_person * 0.1)
	return recoiled_damage

vasa_hitpoints = 576 - applyVeng(number_of_players, teleportedIn) #HP of vasa in the current scale

def simHit(accuracy, maxHit):
	accuracy_rand = random.uniform(0,1)
	hit = random.randint(0, maxHit)
	if accuracy >= accuracy_rand:
		return hit
	else:
		return 0

def simVasaKill():
	no_rigour_hits = teleportedIn
	rigour_hits = (number_of_players - teleportedIn) + 2 * number_of_players
	accurate_rigour_hits = number_of_players
	vasa_hp = vasa_hitpoints
	for i in range(no_rigour_hits):
		vasa_hp -= simHit(rapid_acc, rapid_max)
	for i in range(rigour_hits):
		vasa_hp -= simHit(rapid_rigour_acc, rapid_rigour_max)
	for i in range(accurate_rigour_hits):
		vasa_hp -= simHit(accurate_rigour_acc, accurate_rigour_max)
	if vasa_hp > 0:
		return vasa_hp
	else:
		return 0


def main(x):
	vasa_kills = []
	vasa_remaining = []
	one_crystal_count = 0
	zero_crystal_count = 0
	for i in range(x):
		vasa_kills.append(simVasaKill())
	for i in vasa_kills:
		if i != 0:
			vasa_remaining.append(i)
			one_crystal_count += 1
		else:
			zero_crystal_count += 1
	avg_remaining_hp = sum(vasa_remaining) / len(vasa_remaining)
	avg_remaining_hp = int(avg_remaining_hp)
	zero_crystal_rate = round((zero_crystal_count / (one_crystal_count + zero_crystal_count) * 100), 2)
	print("Vasa was killed with zero crystal " + str(zero_crystal_count) + " times out of " + str(one_crystal_count + zero_crystal_count) + " times overall. When vasa was not killed he was left with an average of " + str(avg_remaining_hp) + "hp")
	print("That means the rate of a zero crystal is: " + str(zero_crystal_rate) + "%.")
	try:
		print("That's 1/" + str(round((zero_crystal_count / (one_crystal_count + zero_crystal_count))**-1, 2)))
	except ZeroDivisionError:
		pass

if __name__ == '__main__':
	main(1000000) #Number of times to run the simulator
