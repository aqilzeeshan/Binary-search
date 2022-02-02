def Binary_search(search,key):
    l=0
    h=len(search)-1
    while l <= h:
        mid = (l+h)//2
        
        mid_element = search[mid]
        print(f"The middle is now {mid} and its element is {mid_element}")

        if key == mid_element:
            print(f"{key} was equal to the middle element. Best case")
            return(mid)
        if key < mid_element:
            h = mid - 1
            print(f"High is now equal to mid - 1: {h}")

        else:
            
            l = mid + 1
            print(f"Low is equal to mid + 1: {l}")
    return("Not found")


list = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
key = float(input("What do you want to search for? "))


ans = Binary_search(list,key)
print(f"The number {key} is at index {ans}")



