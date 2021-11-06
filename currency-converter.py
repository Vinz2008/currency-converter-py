import conversion
print("1.$")
print("2.€")
print("3.£")
currency = int(input("Select the currency that you want to convert : "))

quantity = int(input("What is the quantity of this currency you want to convert "))
total = conversion.convert(currency, quantity)
print(total)
