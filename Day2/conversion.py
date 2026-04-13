# age = input("Enter your age : ")
# print(age + 5)

#it is wrong because input always print string even if it is a number, so age become string,not number. means we cannot add a string with a number.

age = int(input("Enter your age : "))
print (age + 5)

#now string becomes int, we can add both
