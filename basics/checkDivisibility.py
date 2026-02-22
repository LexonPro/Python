#to check number is divisible by 8 and 12
num = int(input("Enter number to check divisibility"))


if num % 8 == 0 and num % 12 == 0:
    print("Divisible by 8 and 12 both")
    
else:
    print("Not divisible")