print("        ARRAY       ")
l=[]
while(True):
    print("1.Insert\n2.Display\n3.Sort\n4.Search\n5.Delete\n6.End")
    c=int(input("\nenter the operation which you want to perform"))
    match c:
        case 1:
            n=int(input("\nenter the size of the array"))
            for i in range(n):
                i=int(input("enter the element"))
                l.append(i)
        case 2:
            print("The array is:",l)
        case 3:
            l.sort()
            print("The Sorted array is",l)
        case 4:
            s=int(input("\nenter the elemet to search"))
            if s in l:
                print("search is done")
            else:
                print("search is failed")
        case 5:
            d=int(input("\nenter the element to delete"))
            l.remove(d)
            print(l)
          
