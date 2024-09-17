number = int(input("Enter a number to see its multiplication table: "))

for s in range(1, 11):
    product = number * s
    print(f"{number} * {s} = {product}")
