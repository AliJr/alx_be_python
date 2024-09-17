number = int(input("Enter a number to see its multiplication table: "))

for n in range(1,11):
    product=number*n
    print(number,"*",n,"=",product)