# 產生一個隨機整數 1~100 
# 讓使用者重複輸入數字去猜
# 猜對印出“終於猜對了！”
# 猜錯告訴他比答案大/小

import random
start = input("請決定隨機數字範圍開始數值")
end = input("請決定隨機數字範圍開結束數值")
start = int(start)
end = int(end)

ran_1 = random.randint(start, end)
count = 0

while True:
	num = input("請猜數字")
	num = int(num)
	count += 1
	if num == ran_1:
		print("終於猜對了！你總共猜了", count, "次")
		break
	elif num > ran_1:
		print("猜錯了，比答案大！")
	elif num < ran_1:
		print("猜錯了，比答案小！")
	print("這是你猜的第", count, "次")
