Marks = int(input("Enter the marks: "))

if Marks < 0 or Marks > 100 :
    print("Invalid ")

elif Marks < 50 :
    print ("Your grade is F ")

elif Marks >= 50 and Marks < 60 :
    print("Your grade is D ")

elif Marks < 70:
    print("Your grade is C ")

elif Marks < 80 :
    print("Your grade is B ")

elif Marks < 90 :
    print("Your grade is A ")

else :
    print ("Your grade is A+ ")