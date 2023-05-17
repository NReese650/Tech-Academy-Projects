num1 = 12
key = False

if num1 == 12:
    if key:
        print('Num1 is equal to Twelve and they have the key!')
    else:
        print('Num1 is equal to Twelve and they DO NOT have the key!')
elif num1 < 12:
    print('Num1 is less than Twelve!')
else:
    print('Num1 is NOT equal to Twelve!')


x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

y = 0

# Convert x to a boolean using bool()
y_bool = bool(y)

print(y_bool)


z = "Hello, world!"

# Use isinstance() to check if z is a string
if isinstance(z, str):
    print("z is a string")
else:
    print("z is not a string")
