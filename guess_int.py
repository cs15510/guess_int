import random

number = random.randint(1, 100)
count = 0
while True:
	guess_int = int(input("請輸入數字(1~100): "))
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