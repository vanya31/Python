#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
#The fourth line should contain the result of integer division
#The fifth line should contain the result of float division

a,b = int(map(input().split()))
print("Sum:", a+b)
print('Difference:', abs((a-b))) #abs() function is used for absolute value
print('Product', a*b)
print("Integer div=", a//b)
print("Float div=", a/b)
