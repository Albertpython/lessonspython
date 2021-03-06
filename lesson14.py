# numbers = [1,2,3,4,5]
# numbers1 = [1,2,3,4,5]
# res = numbers is numbers1
# print(res)

# fruits = ['banan', 'apple', 'chery', 'kiwi']
# print(fruits[1:3])
# print(fruits[:3])
# print(fruits[1:])
# print(fruits[-3:-1])

# fruits = ['banan','apple','cherry']
# fruits.append('orange')
# print(fruits)

# fruits = ['banan','apple', 'cherry']
# fruits.remove('apple')
# print(fruits)

# numbers = [1,2,3,4,5]
# print(numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4])

# numbers = [1,2,3,4,5]
# res = 0
# for x in numbers:
# 	res += x
# print(res)


# fruits = ['banan','apple', 'cherry']
# x = fruits.pop()
# print(x, fruits)


# fruits = ['banan','apple', 'cherry']
# numbers = [1,2,3,4,5]
# fruits.extend(numbers)
# print(fruits)


# numbers = [5,2,3,4,1]
# numbers.sort()
# print(numbers)

# my_list = [1, 324, 12, 4, 5, 0]
# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))
# first = my_list[0]
# for i in my_list:
# 	if i < first:
# 		first = i
# print(first)

# my_list.sort()
# print(my_list[0], my_list[-1])

# import random
# list1 = ['Albert','Arno', 'Razo', 'Garo']
# list2 = ['Mary', 'Vartush', 'Horom', 'Azgush']
# res1 = random.choice(list1)
# res2 = random.choice(list2)
# print(res1 + ' ' + res2)

# boys = ['Albert','Arno', 'Razo', 'Garo']
# girls = ['Mary', 'Vartush', 'Horom', 'Azgush']
# res = []
# for i,j in zip(boys,girls):
# 	c = i + " , " + j
# 	res.append(c)
# print(" ".join(res))

# boys = ['Albert','Arno', 'Razo', 'Garo']
# girls = ['Mary', 'Vartush', 'Horom', 'Azgush']
# res = []
# c = 0
# for i in range(1, len(boys) + 3,2):
# 	boys.insert(1,girls[c])
# 	c += 1
# print(boys)

# my_list = [2, 5, 7, 2, 4]
# first = my_list[0] - my_list[1]

# for i in range(1,len(my_list) - 1):
# 	c = my_list[i] - my_list[i+1]
# 	if c > first:
# 		first = c
# print(first)
