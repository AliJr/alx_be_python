size=int(input("Enter the size of the pattern:"))
row=size
while size>0:
    for r in range(row):
        print("*", end="")
    print()
    size-=1