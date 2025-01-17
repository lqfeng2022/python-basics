high_income = False
good_education = True
unattractive = True

# 1)`and` operator
if high_income and good_education:
    print("Ideal guy")
else:
    print("Not an ideal guy")


# 2)`or` operator
if high_income or good_education:
    print("Ideal guy")
else:
    print("Not an ideal guy")


# 3)`not` operator
if not unattractive:
    print("Ideal guy")
else:
    print("Not an ideal guy")


# 4)Multiple logical operators
if (high_income or good_education) and not unattractive:
    print("Perfect guy")
else:
    print("Not a perfect guy")
