Age = int(input("Enter the Age of the Candidate: "))

if Age >= 18:
    print("vote")
else:
    print("Can't vote")

# In easier way we can also say that
# age = int(input("Enter the age"))
# range = "Vote" if age>=18 else "Can't Vote"
# print (range)
    
# Either in shorter version
# age = int(input("Enter the age: ")
# print("Vote") if age >=18 else print("Can not Vote")