# how to using Zip function
names = ["Bernard","Aaron","Quincy","Ama","Mike"]
ages = [22,21,23,22,25]
gender = ["Male", "Male", "Male", "Female", "Male"]

combined = list(zip(names,ages,gender))
print(combined)

for name, age , gender in combined:
    print(f"{name} is {age} years old and is {gender}"  )
