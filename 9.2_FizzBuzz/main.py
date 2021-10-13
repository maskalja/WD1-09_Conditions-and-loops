limit = int(input("Enter the number between 1 and 100:"))
for i in range(limit):
    if (i+1)%3 == 0 and (i+1)%5 == 0:
        print("fizzbuzz")
    elif (i+1)%3 == 0:
        print("fizz")
    elif (i+1)%5 == 0:
        print("buzz")
    else:
        print(i+1)