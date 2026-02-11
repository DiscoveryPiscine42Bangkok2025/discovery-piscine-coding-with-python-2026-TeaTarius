num_str = input("Enter Number: ")
num = int(num_str)

if num == 0:
    print('This number is both positive and negative.')
elif num >= 1:
    print('This number is positive')
else:
    print('This number is negative.')
