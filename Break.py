low , high = input("Enter the Number : ").split(",")

low = int(low)
high = int(high)

while low <= high:
    print(int(low), end=" ")
    if low % 14 == 0:
        break
    low += 1


# for i in range (int(low), int(high)+1):
#    print (i, end=" ")
# if low % 14 == 0:
#    continue
#    low += 1