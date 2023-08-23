def binarySearch(a,x,si,ei):
    # list should be sorted
    #base case if startIndex si crosses end index ei
    if(si > ei):
        return -1
    mid = (si + ei)//2
    if a[mid] == x:
        return mid
    elif(a[mid]>x):
        return binarySearch(a,x,si, mid - 1)
    else:
        return binarySearch(a,x,mid + 1,si)

li = [int(x) for x in input.split()]
print("Given List: ",li)
li.sort()
print("Sorted list is :", li)
element = int(input("enter the element you want to search: "))
index = binarySearch(li, element,0,len(li)-1)
print(index)
