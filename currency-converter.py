currency = input("What is the currency that you want to convert ?")
quantity = int(input("What is the quantity of this currency you want to convert "))
if currency == "$":
    total = quantity * 0.86
print(total)
