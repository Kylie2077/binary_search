def binary(t,l,number):
    found = False
    tl = t
    
    while found != True:

        if l % 2 == 0:
            mid = (l // 2) - 1
        else:
            mid = l // 2
        if mid > l or mid < 0:
            return -1
            break
        if number == t[mid]:
            found = True
            return tl.index(number) + 1
        elif number > t[mid]:
            t = t[mid+1:]
            l = len(t)
        elif number < t[mid]:
            t = t[:mid]
            l = len(t)
            
lst = []
while len(lst) != 10:
    i = int(input(f"Enter the number {len(lst)+1}: "))
    lst.append(i)

lst.sort()
number = int(input("Enter the number you want to search: "))
llst = len(lst)
b = binary(lst,llst,number)
if b == -1:
    print("The number you're lookig for is not in the list.")
else:
    print(f"The number is in index {b} of the list.")
