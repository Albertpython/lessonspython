# import random
# python_team = ['Albert', 'Meri', 'Arno', 'Razo', 'Arsho', 'Sargis']
# random.shuffle(python_team)
# count = 1
# for i,j in zip(python_team[:3], python_team[3:]):
# 	print(count, i, j)
# 	count += 1


# thisdict = {'name':'Aram', 'year':1994}
# thisdict['year'] = 2014
# thisdict['age'] = 26
# print(thisdict)


# thisdict = {'name':'Aram', 'year':1994}
# del thisdict['year']
# print(thisdict)

# import datetime
# person = dict(name = 'Sargis', year = 17, color = 'white', country = 'Vagharshapat')
# x = datetime.datetime.now()
# print(x.year - person['year'])


# for i in person:
# 	print(person[i])

# for i in person:
# 	print(i)

# for i,j in person.items():
# 	print(i,j)

# for i in person.values():
# 	print(i)


# person = dict(name = 'Sargis', year = 17, color = 'white', country = 'Vagharshapat')
# count = 0
# for i in person:
# 	count += 1
# print(count)


# person = dict(name1 = 'Meri', name2 = 'Albert', name3 = 'Arno', name4 = 'Razo', name5 = 'Arsen', name6 = 'Arsen')
# count = 0
# if 'Arsen' in person.values():
# 	for i in person.values():

# 		if i == 'Arsen':
# 			count += 1
		

# 	print(count,"Yes")

# else:
# 	print(count,"No")


# list1 = ['Ani', 'Ani', 'Aram']
# list2 = []
# for i in list1:
# 	if list1.count(i) > 1:
# 		pass
# 	else:
# 		list2.append(i)

# print(list2)




login = input("Login: ")
password_chars = ('!', '@', '#', '$', '%')


while True:
	password = input("Password: ")

	if len(password) < 8: 
		print('your password is not strong')
		continue

	char_count = 0
	number_count = 0

	for i in password:
		if i in password_chars:
			char_count += 1
		elif i.isdigit():
			number_count += 1

	if char_count < 2:
		print('Your password must be have two chars', )
		continue

	if number_count < 2:
		print('Your password must be have two numbers')
		continue

	if password[0].isalpha() and password[0].islower():
		print('First letter must be upper')
		continue

	else:
		print('Strong Password')
		break


while True:
	email = input("Email: ")

	if len(email) < 10:
		print("Input new email")
		continue

	
	for j in email:
		if j.isdigit():
			print("input new email")
			continue
		if email[0] == '@' and email[1] == '.':
			print("input new email")
			continue

		elif email[0] == '.' and email[1] == '@':
			print("input new email")
			continue

	else:
		print("your email is strong")
		break





while True:
	phone = input("Phone number: ")

	if len(phone) < 9:
		print("Input new phone number")
		continue
	for x in phone:
		if x.isalpha():
			print("Input new phone number")
			continue

	else:
		print('Your phone is True')
		break



		

