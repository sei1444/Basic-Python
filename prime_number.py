a = int(input("aの値を入力: "))


for i in range(2, a):
	if a % i == 0:
		b = 1
		break
if b == 1:
	print("素数でない")
else:
	print("素数である")

	
            
    


