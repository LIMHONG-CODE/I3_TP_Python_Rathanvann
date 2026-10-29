print('int("7") + 3.5 -> ', int("7") + 3.5)
print("str(10) * 3 -> ", str(10) * 3)
print('bool(""), bool(" ") -> ', bool(""), bool(" "))
print("int(3.99) -> ", int(3.99))
print('float("1e3") -> ', float("1e3"))
print('int(True) + float("2.5") -> ', int(True) + float("2.5"))
print("round(2.5), round(3.5) -> ", round(2.5), round(3.5))
print("type(10 / 2) -> ", type(10 / 2))

def safe_int(text):
    try:
        return int(float(text.strip()))
    except(ValueError, AttributeError, OverflowError):
        return None
    
for sample in ["42", " -8 ", "3.9", "abc", ""]: 
    print(repr(sample), "->", safe_int(sample)) 

first_text = input("User must be enter a first number: ")
second_text = input("User must be enter a second number: ")

first_number = safe_int(first_text)
second_number = safe_int(second_text)

if first_number is None or second_number is None:
    print("Please enter two valid number.")
else:
    print("Sum of two numbers is = ", first_number + second_number)
