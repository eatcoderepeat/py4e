largest = None
smallest = None

while True:
    num = input("Enter Number: ")
    #break statement
    if num == 'done':
        break

    #check input type is valid
    try:
        num = int(num)
    except ValueError:
        try:
            num = float(num)
        except ValueError:
            print("Invalid input")
            continue

    #first number entered
    if largest is None:
        largest = num
        smallest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print('Minimum is', smallest)
