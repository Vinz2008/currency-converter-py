def convert(currency, quantity):
    print("1.$")
    print("2.€")
    print("3.£")
    currency2 = int(input("Select the currency you want to convert to : "))
    if currency == currency2:
        total = quantity
    if currency == 1:
        if currency2 == 2:
            total = quantity * 0.87
        if currency2 == 3:
            total = quantity * 0.74
    if currency == 2:
        if currency2 == 1:
            total = quantity * 1.16
        if currency2 == 3:
            total = quantity * 0.86
    if currency == 3:
        if currency2 == 1:
            total = quantity * 1.35
        if currency2 == 2:
            total = quantity * 1.17
    return total
