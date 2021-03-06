import random
ch = random.choice('up')
point = 0
if ch == 'u':
	print("User start: ")
	while True:

		while True:
			user = input("(1-3): ")
			end = 4

			if point > 18:
				end = 22 - point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					print("User -", point, "+", user, "=", point + user)
					point += user
					break
				else:
					print("please input betwen: 1 - :", end - 1)
			else:
				print("please input only number: ")
		if point == 21:
			print("win pc")
			break
		if point > 18:
			end = 22- point

		pc = 4 - point % 4
		print("Pc -", point, "+", pc, "=", point + pc)
		point += pc

		if point == 21:
			print("win user")
			break
else:
	print("Pc start: ")
	while True:
		pc = random.randint(1,3)




	