import random
import time
a = ["Bầu", "Cua", "Tôm", "Cá", "Gà", "Nai"]

# Hàm rung bầu cua
def baucua():
	b = random.choice(a) 
	c = random.choice(a)
	d = random.choice(a)
	if b == c and b == d :
		print("-------------")
		print("[ 3", b, " ]")
		print("-------------")
	elif b == c :
		print("---------------------")
		print("[ 2", b, " ] [ 1", d, " ]")
		print("---------------------")
	elif b == d :
		print("---------------------")
		print("[ 2", b, " ] [ 1", c, " ]")
		print("---------------------")
	elif c == d :
		print("----------------------")
		print("[ 2", c, " ] [ 1", b, " ]")
		print("----------------------")
	else :
		print("--------------------------------")
		print("[ 1", b, " ] [ 1", c, " ] [ 1", d, " ]")
		print("--------------------------------")

batdau = True

while batdau == True :
	choigame = input("Bạn muốn chơi game bầu cua? yes or no\t")
	if choigame.startswith("y") : # Nếu nhập chữ bắt đầu bằng y sẽ chạy vòng 
		i = 4
		while i > 1 :
			time.sleep(1) # Chờ 1 giây
			i = i - 1
			print(i, "...")

			if i == 1:
				print("Mở cái bát!")
				time.sleep(3)

		baucua()
	else :
	    print("Chào tạm biệt!")
	    break