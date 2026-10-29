def letter_grade(score):
    if score < 0 or score > 100:
        return("Invalid.")
    elif score >= 97:
        return"A+"
    elif score >= 90:
        return"A"
    elif score >= 80:
        return"B"
    elif score >= 70:
        return"C"
    elif score >= 60:
        return"D"
    else:
        return"F"

for score in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(f"{score:5} -> {letter_grade(score)}")

# A+ must be tested before A because every A+ score is also >= 97.
# If >= 90 is checked first, scores such as 99 would return A, not A+.