# names = ['Razmik', 'Albert', 'Meri', 'Sargis','Arsho']

# res = [i for i in names if len(i) == max([len(i) for i in names])]
# print(', '.join(res))

# c = []
# for i in names:
# 	c.append(len(i))
# max_l = max(c)

# for i in names:
# 	if len(i) == max_l:
# 		print(i)

# my_list = ['Meri', 20, True, ('Abul', 'Arno'), 5.2, ['Ab', 'Mer']]
# print(my_list)

# my_list = ['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo', 'Hp']

# user = input("Pc: ").title()
# if user in my_list:
# 	print("Yes", my_list.count(user))
# else:
# 	print("No", my_list.count(user))



# chars = ('!', '@', '#', '$', '%', '&', '*')

# while True:
# 	password = input("Password: ")

# 	if len(password) < 8:
# 		print('Your password lenght is less then 8')
# 		continue

# 	chars_counts = 0
# 	number_counts = 0

# 	for i in password:
# 		if i in chars:
# 			chars_counts += 1
# 		elif i.isdigit():
# 			number_counts += 1

# 	if chars_counts < 2:
# 		print('Your password must be have two chars', chars)
# 		continue

# 	if number_counts < 2:
# 		print('Your password must be have two numbers')
# 		continue

# 	if password[0].isalpha() and password[0].islower():
# 		print('First letter must be upper')
# 		continue

# 	print('Strong Password')
# 	break

# link = 'https://www.youtube.com/watch?v=I020GSBjAzA'
# count = 0
# for i in link:
# 	count += 1
# 	if i == '=':
# 		break
# print(link[link.index('=')+1:])


# user = input("word: ")
# if user == user [::-1]:
# 	print("Yes")
# else:
# 	print("No")


# list1 = ["Albert", "Meri", "Arno", "Razo", "Albert"]
# list2 = []
# for x in list1:
# 	if x not in list2:
# 		list2.append(x)
# print(list2)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list1:
	if i % 2 != 0:
		list1.remove(i)
print(list1) 


