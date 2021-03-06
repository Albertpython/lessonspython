# a = ()
# b = tuple()
# print(type(a))
# print(type(b))

# cars = ("bmw", "audi", 2021)
# client = input("whitch car we want? ").lower()
# year = int(input("Year: "))

# if client in cars and year in cars:
# 	print("Yes we have", client.title())
# else:
# 	print("Sorry we don't have", client.title())

# models = ("samsung", "iphone", "nokia")
# colors = ("red", "yellow", "black")
# phone = input("Phone?: ")
# color = input("Color?: ")

# if phone in models:
# 	if color in colors:
# 		print("Yes we have color", color.title(), "Yes we have model", phone.title())
# 	else:
# 		print("Yes we have model", phone.title(),"Sorry we don't have color", color.title())
# else:
# 	print("Sorry we don't have phone", phone.title(),"Sorry we don't have color", color.title())


# my_tuple = ("Meri", "Anne", "Anna", "Gexam")
# print(sorted(my_tuple))
# my_number = (33,2,4,1,23,4)
# print(sorted(my_number) [::-1])
# res = reversed(my_tuple)
# print(tuple(res))

# tupl = ("physics", "chemistry", 1997, 2000)
# print(tupl.__sizeof__())

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = ("apple", "banana", "cherry", "kiwi")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)


# num = [10,20,30,(10,20),40]
# c = 0 
# for n in num:
# 	if isinstance (n, tuple):
# 		break
# 	c += 1
# print(c)


tup = ("e", "x", "e", "r", "c", "i", "s", "e", "s")
mystr = ''.join(tup)
print(mystr)
