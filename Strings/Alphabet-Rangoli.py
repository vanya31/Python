def print_rangoli(size):
    # your code goes here
    for i in  range((size*2)-1):
        for j in range (size*size):
            print("_")

size=int(input())
print_rangoli(size)
     