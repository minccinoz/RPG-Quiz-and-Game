a = 0
b = 0
c = 0
d = 0
e = 0

def tally(x):
	if x == "A":
		global a
		a += 1
		return a
	if x == "B":
		global b
		b += 1
		return b
	if x == "C":
		global c
		c += 1
		return c
	if x == "D":
		global d
		d += 1
		return d
	if x == "E":
		global e
		e += 1
		return e


username = input("Welcome to our game. Enter your name: ")

print("Welcome",username,".")
print("Q1: If you were caught in a position to defend yourself, which weapon would you prefer?")
print("A: Sword")
print("B: Wand (assuming you could cast spells)")
print("C: Fists")
print("D: Daggers")
print("E: Peace and love, man")
answer1 = input("Choose one: ")
tally(answer1)

print("Q2: How do you tend to handle conflicts?")
print("A: Speak my mind and use force only if need be.")
print("B: Cast brujería on my enemies.")
print("C: Fight them. No one wants to catch these hands.")
print("D: Secretly plot their demise. They better sleep with one eye open.")
print("E: I am a tender soul that cannot handle conflict.")
answer2 = input("Choose one: ")
tally(answer2)

print("Q3: If you were a superhero, who would you be?")
print("A: Superman")
print("B: Doctor Strange")
print("C: Wonderwoman")
print("D: Batman")
print("E: Aquaman")
answer3 = input("Choose one: ")
tally(answer3)

print("Q4: If you were a supervillain, who would you be?")
print("A: Two-Face")
print("B: Riddler")
print("C: Bane")
print("D: Catwoman")
print("E: Poison Ivy")
answer4 = input("Choose one: ")
tally(answer4)

print("Q5: What mythical creature would you be?")
print("A: Centaur")
print("B: Elf")
print("C: Ogre")
print("D: Basilisk")
print("E: Angel")
answer5 = input("Choose one: ")
tally(answer5)

print("Q6: Which personality trait best describes you?")
print("A: Courageous")
print("B: Wise")
print("C: Powerful")
print("D: Cunning")
print("E: Compassionate")
answer6 = input("Choose one: ")
tally(answer6)

print("Q7: Which of the following seems to be a recurring problem for you?")
print("A: I tend to see things in black-and-white, good-or-bad.")
print("B: I tend to overanalyze situations.")
print("C: I tend to lose my temper too quickly.")
print("D: I tend to be sadistic.")
print("E: I tend to have my kindness taken for granted.")
answer7 = input("Choose one: ")
tally(answer7)

print("Q8: What role do you see yourself playing in an action movie?")
print("A: The Hero")
print("B: The Sidekick")
print("C: The Rival")
print("D: The Anti-hero")
print("E: The Group Mom")
answer8 = input("Choose one: ")
tally(answer8)

print("Q9: Which occupation below would you choose?")
print("A: Police officer")
print("B: College professor")
print("C: Professional Boxer")
print("D: Mercenary")
print("E: EMT worker")
answer9 = input("Choose one: ")
tally(answer9)

print("Q10: Which book/series is your favorite out of the following?")
print("A: Divergent")
print("B: Harry Potter")
print("C: Sun Tzu's Art of War")
print("D: V for Vendetta")
print("E: The Giving Tree")
answer10 = input("Choose one: ")
tally(answer10)

print("Q11: Pick a virtue out of the following (shoutout 2 whoever gets the reference):")
print("A: Candor")
print("B: Erudite")
print("C: Abnegation")
print("D: Dauntless")
print("E: Amity")
answer11 = input("Choose one: ")
tally(answer11)

def result():
	if a > b and a > c and a > d and a > e:
		print("You are a Knight!")
	elif b > a and b > c and b > d and b > e:
		print("You are a Mage!")
	elif c > a and c > b and c > d and c > e:
		print("You are a Tank!")
	elif d > a and d > b and d > c and d > e:
		print("You are an Assassin!")
	elif e > a and e > b and e > c and e > d:
		print("You are a Healer!")
	else:
		print("You're 2 complicated. Please take quiz again and change like one of your answers.")

result()
