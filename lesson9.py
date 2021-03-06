# from random import randint as r

# pc = r(0,5)
# user = int(input("User: ( 0-5"))
# user_point, pc_point = 0,0

# if pc == user:
# 	user_point += 1
# 	print(pc, user, "good user", user_point)
# else:
# 	pc_point += 1
# 	print(pc, user, "good pc", pc_point)

# pc = r(0,5)
# user = int(input("User: ( 0-5"))

# if pc == user:
# 	user_point == 1
# 	print(pc, user, "good user", user_point)
# else:
# 	pc_point += 1
# 	print(pc, user, "good pc", pc_point)

# if user_point == pc_point:
# 	pc = r(0,5)
# 	user = int(input("User: (0-5)"))
# 	if pc == user:
# 		user_point += 1
# 		print(pc, user, "win user", user_point)
# 	else:
# 		pc_point += 1
# 		print(pc, user, "win pc", pc_point)

# else:
# 	if user_point == 2:
# 		print("Win user")
# 	else:
# 		print("win pc")


# number = int(input("Number "))
# first =  number % 10
# second = number // 10 % 10
# third = number // 100 % 10
# fourth = number // 1000

# print(str(first) + str(second) + str(third) + str(fourth))

# S = 12
# T_pc = 3
# T_user = T_pc + T_pc * 0.1
# V_user = S / T_user
# print(V_user)
import random
user_followers = int(input("Followers "))
pc_followes = random.randint(100,1000)
tokos = random.randint(20,100)
if user_followers - user_followers * tokos / 100 == pc_followes :
	print("Bloger user")
else:
	print("Bloger pc")

