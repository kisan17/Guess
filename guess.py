import random
import math
lower=int(input("Enter the lower bound:-"))
upper=int(input("Enter the upper bound:-"))

x=random.randint(lower,upper)

print("you have only",round(math.log(upper-lower+1,2)),"chances to guess the integer!\n")

count=0

while count <math.log(upper-lower+1,2):
	count +=1

	guess=int(input("Enter the number:-"))

	if x==guess:
		print("Congrats! you have guess right number")
		break

	elif x<guess:
		print("try again!you guess the number which is so higher.")

	elif x>guess:
		print("Try again!you have guess the number which is small.")

if count>=math.log(upper-lower+1,2):
	print("\n the number is %d" %x )
	print("\t Better next time")
