print("Hello user! This program converts kilometers to miles.")

while True:
    km = float(input("Please, enter the number of kilometers: "))
    miles = km * 0.6213712
    print("{0} km converted to miles is {1} miles".format(km, miles))
    ans = input("Do you want to do another conversion?: ")
    if ans.lower() != "yes":
        break
print("Goodbye!")
