def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    energy_cost = tier1 * 480 + tier2 * 610 + tier3 * 730
    before_vat = energy_cost + 2000
    total = before_vat * 1.10
    return round(total)


for consumption in (0, 35, 50, 120, 200, 350):
    bill = electricity_bill(consumption)
    usd = bill / 4100
    print(f"{consumption:3} kWh -> {bill:>7,} riel (≈ {usd:.2f} USD)")

try:
    user_kwh = float(input("Problem 9 - Enter monthly consumption in kWh: "))
    user_bill = electricity_bill(user_kwh)
    if user_bill is None:
        print("Consumption cannot be negative.")
    else:
        print(f"Your bill: {user_bill:,} riel (≈ {user_bill / 4100:.2f} USD)")
except ValueError:
    print("Please enter a valid number for kWh.")