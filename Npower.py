Base = int(input("Enter the Base value: "))
expo = int(input("Enter the Expo value: "))

result = 1

#i = 1
#while i <= expo:
   # result *= Base
  #  i += 1
  #  print(result)

#for i in range (0, expo):
  #  result = result * Base
    #print(result)

for expo in range(expo, 0 ,-1):
    result *= Base
    print(result)