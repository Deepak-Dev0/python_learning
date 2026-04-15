list = []
num=int(input("Enter how many numbers you want to insert : "))
for i in range(num,0,-1):
	x = int(input(f"Enter one number at a time,upto {i} times : "))
	list.append(x)
print(list)
