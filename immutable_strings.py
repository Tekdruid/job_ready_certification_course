my_var = "abcdefg"
print(my_var)
letter = my_var[0]
print(letter)

# This will not work:
# my_var[0] = "1"

# Instead use this:
my_var = "1" + my_var[1:]

print(my_var)