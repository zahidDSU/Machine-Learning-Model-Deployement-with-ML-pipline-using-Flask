try:
    age = int(input("Enter your age: "))
except(Exception) as e:
    
    print("Not a Valid age")

else:
    print("Age: ", age)