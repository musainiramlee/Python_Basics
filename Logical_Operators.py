has_good_rating = True
has_high_income = True
has_high_saving = False
has_criminal_record = True

if (has_good_rating or has_high_income) and not has_criminal_record:
    print("Eligible for loan with normal interest")
elif has_high_saving and not has_criminal_record:
    print("Eligible for loan with higher interest")
else:
    print("Loan application rejected")


