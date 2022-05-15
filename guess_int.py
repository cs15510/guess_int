import random

guess_rang = int(input("請輸入你想猜的範圍: "))
number = random.randint(1, guess_rang)
count = 0
while True:
	guess_int = int(input("請輸入數字(1~"+str(guess_rang)+"): "))
	count += 1
	if guess_int == number:
		print("終於猜對了, 這是你猜的第", count, "次")
		break
	else:
		if guess_int > number:
			print("比答案大,", end = " ")
		else:
			print("比答案小,", end = " ")
	print("這是你猜的第", count, "次")