num =[10,35,67,82,49]
total=0
print("list : ",num)
for i in num:
	temp_total=total+i
	print(total," + ",i," = ",temp_total)
	total +=i
print("Sum of list = ",total)
