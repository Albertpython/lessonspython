# first = int(input("Number: "))
# second = int(input("Number: "))

# if first >= second:
# 	start = first
# else:
# 	start = second
# for i in range(start, first * second + 1):
# 	if i % first == 0 and i % second == 0:
# 		print(i)
# 		break


# first = int(input("Number: "))
# second = int(input("Number: "))
# if first >= second:
# 	strat = first
# else:
# 	start = second
# while True:
# 	if start % first == 0 and start % second == 0:
# 		print(start)
# 		break
# 	start += 1


# even =0
# odd = 0
# for i in range(1,101):
# 	if i % 2 ==0:
# 		even +=1
# 	else:
# 		odd +=1
# print(even, odd)


# x,y = 0,1
# while x < 40:
# 	print(x)
# 	x,y = y,x+y


# letters = 0
# number = 0
# string = "python 3.9"
# for i in string:
# 	if i.isdigit():
# 		letters += 1
# 	elif i.isalpha():
# 		number += 1 
# print(letters, number)


# count = 0
# number = int(input("Number: "))
# for x in str(number):
# 	count += int(x) 
# print(count)	


# count = 1
# number = int(input("Number: "))
# for i in range(1, number + 1):
# 	count *= i
# print(count)

import math
import time
number = int(input("Number: "))
start = time.time()

for i in range(2, number):
	if number % i == 0:
		print("No")
		break
else:
	print("Yes")
end = time.time()
print(end - start)