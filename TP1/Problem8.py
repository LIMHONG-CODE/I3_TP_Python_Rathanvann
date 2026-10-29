def describe(*numbers, decimals = 2, label = "Data"):
    if not numbers:
        print(f"{label}: is not value.")
        return None

    count = len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    mean = round(sum(numbers)/count, decimals)

    print(
        f"{label} is n= {count} max= {maximum} min= {minimum}"
        f" mean= {mean}"
    )
    return count, maximum, minimum, mean

def make_tag(text, **style):
    attributes = " ".join(f'{key}="{value}"' for key, value in style.items())
    if attributes:
        return f"<span {attributes}>{text}</span>"
    return f"<span>{text}</span>"


square = lambda x: x ** 2
is_adult = lambda age: age >= 18

describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()
print(make_tag("Hello", color="red", size=14))
print(square(9), is_adult(17), is_adult(21))