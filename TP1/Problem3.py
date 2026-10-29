def celsius_to_fahrenheit(c, round_to=1):
    return round(c * 9 / 5 + 32, round_to)

def fahrenheit_to_celsius(f, round_to=1):
    return round((f - 32) * 5 / 9, round_to)

print(" °C | °F")
print("----+-----")
for celsius in range(0, 101, 20):
    print(f"{celsius:3} | {celsius_to_fahrenheit(celsius):.1f}")

print(f"98.6 °F = {fahrenheit_to_celsius(98.6):.1f} °C")
fahrenheit = celsius_to_fahrenheit(37)
print(f"37 °C = {fahrenheit:.1f} °F; converted back = "
      f"{fahrenheit_to_celsius(fahrenheit):.1f} °C")
print(f"37 °C to fahrenheit (3 decimals) = {celsius_to_fahrenheit(37, round_to=3)}")