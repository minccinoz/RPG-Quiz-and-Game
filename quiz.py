from graphics import *
import random

# FIRST PT. GUI PROGRAM

win = GraphWin("Mario, Peach, Bowser!", 500, 500)
win.setBackground("white")

t = Text(Point(250, 100), "Welcome to Mario 'Rock, Paper, Scissors'!\n\nPick 'Mario', 'Peach', or 'Bowser'.")
t.setSize(25)
t.draw(win)

e = Entry(Point(250, 200), 15)
e.draw(win)

m = win.getMouse()
user_choice = e.getText()
if user_choice == "Mario":
	user_choice = "Mario"
elif user_choice == "Peach":
	user_choice = "Peach"
elif user_choice == "Bowser":
	user_choice = "Bowser"
else:
	user_choice = "Bowser"

t.undraw()
e.undraw()


# Show what the user chose
imm = Image(Point(250, 250), "mario.gif")
imp = Image(Point(250, 250), "peach.gif")
imb = Image(Point(250, 250), "bowser.gif")

t2 = Text(Point(250, 100), "You chose: " + user_choice)
t2.setSize(25)

if user_choice == "Mario":
	imm.draw(win)
	win.setBackground("salmon")
elif user_choice == "Peach":
	imp.draw(win)
	win.setBackground("pink")
elif user_choice == "Bowser":
	imb.draw(win)
	win.setBackground("purple")

t2.draw(win)
t3 = Text(Point(250, 450), "Click to play against computer!")
t3.draw(win)

win.getMouse()

# Flip the coin!
imm.undraw()
imp.undraw()
imb.undraw()
t2.undraw()
ch = random.choice(["Mario", "Peach", "Bowser"])
t3.undraw()

t4 = Text(Point(250, 450), "It's a TIE!")
t4.setSize(25)
t5 = Text(Point(250, 450), "You WIN!")
t5.setSize(25)
t6 = Text(Point(250, 100), "Mario defeated Bowser!")
t7 = Text(Point(250, 100), "Peach charmed Mario!")
t8 = Text(Point(250, 100), "Bowser kidnapped Peach!")
t9 = Text(Point(250, 450), "You LOSE!")
t9.setSize(25)

if ch == user_choice:
	t10 = Text(Point(250, 100), "Computer chose: " + ch)
	t4.draw(win)
elif ch == "Mario" and user_choice == "Peach":
	t7.draw(win)
	t5.draw(win)
elif ch == "Peach" and user_choice == "Mario":
	t7.draw(win)
	t9.draw(win)
elif ch == "Bowser" and user_choice == "Mario":
	t6.draw(win)
	t5.draw(win)
elif ch == "Mario" and user_choice == "Bowser":
	t6.draw(win)
	t9.draw(win)
elif ch == "Peach" and user_choice == "Bowser":
	t8.draw(win)
	t5.draw(win)
elif ch == "Bowser" and user_choice == "Peach":
	t8.draw(win)
	t9.draw(win)
else:
	t9.draw(win)

if ch == "Mario":
	imm.draw(win)
elif ch == "Peach":
	imp.draw(win)
else:
	imb.draw(win)




win.getMouse()
win.close()


# SECOND PT. SHORT STORY ASSIGNMENT

print("\nWelcome to 'A day in the life of a procrastinator'.\n\nYou have an entire week to complete this assignment.\nWill you work on it now?\n")

choice1 = input("A: Yes\nB: No ")

if choice1 == 'A':
	print("\nWow, so responsible.")
	print("You type one sentence and feel accomplished and very much like an adult.\n")
	print("Fast forward: it's Thursday and you still haven't finished your assignment.")
	print("You still have some time, but you'd like the weekend free so you can chill with friends (or by yourself if you have no friends).")
	print("What will you do?\n")

	choice2a = input("A: Work on assignment.\nB: Get starbucks. ")
	if choice2a == 'A':
		print("\nYou attempted the assignment but got bored.")
		print("You decided to get starbucks anyway (or any cafe of your choice)\nbecause maybe caffeine will give you the boost you need.")
		print("\nYou get your fix then run back home to work on your assignment.")
		print("You get a burst of energy to do anything and everything unrelated to your assignment.\n")
		print("What will you do?")
		choice3a = input("\nA: Work on assignment.\nB: Clean entire house. ")

		if choice3a == 'A':
			print("\nThat's cute.\n")
			print("But as soon as you get on the computer you start organizing your iTunes library and jamming out to old tunes you forgot you even had.")
			print("While you're at it, you find a compilation of adorable and funny cat/dog videos.\n")
			print("This takes hours of your time.\n")
			print("But don't worry: maybe Sunday will be more productive.\n")
			print("Fast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this #*)%&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
			if choice4a == 'B':
				print("You stay up watching Netflix.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
		
		if choice3a == 'B':
			print("\nYour parents would be so proud. (But not proud that you've procrastinated.)\n")
			print("Fast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this #*)%&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")

	if choice2a == 'B':
		print("\nYou decided to get starbucks. Caffeine helps you concentrate, right?")
		print("\nYou get your fix then run back home to work on your assignment.")
		print("You get a burst of energy to do anything and everything unrelated to your assignment.\n")
		print("What will you do?\n")
		choice3a = input("A: Work on assignment.\nB: Clean entire house. ")

		if choice3a == 'A':
			print("\nThat's cute.\n")
			print("But as soon as you get on the computer you start organizing your iTunes library and jamming out to old tunes you forgot you even had.")
			print("While you're at it, you find a compilation of adorable and funny cat/dog videos.\n")
			print("This takes hours of your time.\n")
			print("But don't worry: maybe Sunday will be more productive.\n")
			print("Fast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this f#&$(*&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
			if choice4a == 'B':
				print("You stay up watching Netflix.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")

		if choice3a == 'B':
			print("\nYour parents would be so proud. (But not proud that you've procrastinated.)")
			print("\nFast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this #*)%&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
			
			if choice4a == 'B':
				print("\nYou stay up watching Netflix.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")

					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")

if choice1 == 'B':
	print("\nThat's ok, you still have the rest of the week.")
	print("\nFast forward: it's Thursday and you still haven't finished your assignment.")
	print("You still have some time, but you'd like the weekend free so you can chill with friends (or by yourself if you have no friends).")
	print("What will you do?\n")

	choice2a = input("A: Work on assignment.\nB: Get starbucks. ")
	if choice2a == 'A':
		print("\nYou attempted the assignment but got bored.")
		print("You decided to get starbucks anyway (or any cafe of your choice)\nbecause maybe caffeine will give you the boost you need.")
		print("You get your fix then run back home to work on your assignment.")
		print("You get a burst of energy to do anything and everything unrelated to your assignment.\n")
		print("What will you do?")
		choice3a = input("\nA: Work on assignment.\nB: Clean entire house. ")

		if choice3a == 'A':
			print("\nThat's cute.\n")
			print("But as soon as you get on the computer you start organizing your iTunes library and jamming out to old tunes you forgot you even had.")
			print("While you're at it, you find a compilation of adorable and funny cat/dog videos.\n")
			print("This takes hours of your time.\n")
			print("But don't worry: maybe Sunday will be more productive.\n")
			print("Fast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this #*)%&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.\n")
				print("It is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
			if choice4a == 'B':
				print("\nYou stay up watching Netflix.\n")
				print("It is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
		
		if choice3a == 'B':
			print("\nYour parents would be so proud. (But not proud that you've procrastinated.)")
			print("\nFast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this #*)%&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")

	if choice2a == 'B':
		print("\nYou decided to get starbucks. Caffeine helps you concentrate, right?")
		print("\nYou get your fix then run back home to work on your assignment.")
		print("You get a burst of energy to do anything and everything unrelated to your assignment.\n")
		print("What will you do?")
		choice3a = input("\nA: Work on assignment.\nB: Clean entire house. ")

		if choice3a == 'A':
			print("\nThat's cute.")
			print("\nBut as soon as you get on the computer you start organizing your iTunes library and jamming out to old tunes you forgot you even had.")
			print("While you're at it, you find a compilation of adorable and funny cat/dog videos.\n")
			print("This takes hours of your time.\n")
			print("But don't worry: maybe Sunday will be more productive.\n")
			print("Fast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this f#&$(*&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?\n")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
			if choice4a == 'B':
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")

		if choice3a == 'B':
			print("\nYour parents would be so proud. (But not proud that you've procrastinated.)")
			print("\nFast forward: Sunday rolls around and you made a promise to yourself that this would be the day you finally get to this #*)%&@ assignment.")
			print("But there are new episodes out of that show you like and life is stressful.")
			print("Perfect way to unwind on a lazy Sunday.")
			print("\nWhat will you do?")
			choice4a = input("\nA: Work on assignment.\nB: Watch Netflix. ")

			if choice4a == 'A':
				print("\nYou work for about a half hour, but the suspense is killing you slowly.")
				print("You stay up watching Netflix instead.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")
					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")
			
			if choice4a == 'B':
				print("\nYou stay up watching Netflix.")
				print("\nIt is now 3AM and the assignment is due tomorrow.")
				print("What do you do?")
				choice5a = input("\nA: Cry.\nB: Cry. ")

				if choice5a == 'A' or 'B':
					print("\nYou cry in fetal position and contemplate your life.")
					print("\nIt is morning-- and your class is at noon!\nWhat do you do?")
					choice6a = input("\nA: FINISH THE THING.\nB: FINISH THE THING. ")

					if choice6a == 'A' or 'B':
						print("\nSee, that wasn't so bad.")
						print("You finished it and were only 15 minutes late to class\nbecause your printer ran out of ink and MTA delays.")
						print("\nThe prof didn't seem to mind though.\n\nYou're safe for another week.")		