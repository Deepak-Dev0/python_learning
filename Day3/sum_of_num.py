n = int(input("Enter a number : "))
total=0
for i in range (1,n+1):
	print(i)
	total += i
print(f"sum of all numbers before and including {n} is : ",total)
