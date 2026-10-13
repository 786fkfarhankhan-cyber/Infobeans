print("*" * 10 , " Welcome To D-Mart ","*" * 10)

name = input("Enter your name = ")
gender = input("Enter Your Gender (Male/Female) = ")

# Items :-
item1_name = input("Enter Item1 Name = ")
item1_qty = int(input("Enter a Quantity You Purchase for item1 = "))
item1_price = int(input("Enter Item1 Price = "))
item1_total = item1_qty * item1_price

# Discount check (sirf item 1 ke liye special condition)
if item1_qty > 4:
    item1_discount = 5
else:
    item1_discount = 0
item1_after_discount = item1_total - (item1_total * item1_discount / 100)

item2_name = input("Enter Item2 Name = ")
item2_qty = int(input("Enter a Quantity You Purchase for item2 = "))
item2_price = int(input("Enter Item2 Price = "))
item2_total = item2_qty * item2_price
item2_after_discount = item2_total

item3_name = input("Enter Item3 Name = ")
item3_qty = int(input("Enter a Quantity You Purchase for item3 = "))
item3_price = int(input("Enter Item3 Price = "))
item3_total = item3_qty * item3_price
item3_after_discount = item3_total

item4_name = input("Enter Item4 Name = ")
item4_qty = int(input("Enter a Quantity You Purchase for item4 = "))
item4_price = int(input("Enter Item4 Price = "))
item4_total = item4_qty * item4_price
item4_after_discount = item4_total

item5_name = input("Enter Item5 Name = ")
item5_qty = int(input("Enter a Quantity You Purchase for item5 = "))
item5_price = int(input("Enter Item5 Price = "))
item5_total = item5_qty * item5_price

# Discount check (sirf item 5 ke liye special condition)
item5_discount = 10
item5_after_discount = item5_total - (item5_total * item5_discount / 100)

item6_name = input("Enter Item6 Name = ")
item6_qty = int(input("Enter a Quantity You Purchase for item6 = "))
item6_price = int(input("Enter Item6 Price = "))
item6_total = item6_qty * item6_price
item6_after_discount = item6_total

item7_name = input("Enter Item7 Name = ")
item7_qty = int(input("Enter a Quantity You Purchase for item7 = "))
item7_price = int(input("Enter Item7 Price = "))
item7_total = item7_qty * item7_price
item7_after_discount = item7_total

item8_name = input("Enter Item8 Name = ")
item8_qty = int(input("Enter a Quantity You Purchase for item 8 = "))
item8_price = int(input("Enter Item8 Price = "))
item8_total = item8_qty * item8_price
item8_after_discount = item8_total

item9_name = input("Enter Item9 Name = ")
item9_qty = int(input("Enter a Quantity You Purchase for item9 = "))
item9_price = int(input("Enter Item9 Price = "))
item9_total = item9_qty * item9_price
item9_after_discount = item9_total

item10_name = input("Enter Item 10 Name = ")
item10_qty = int(input("Enter a Quantity You Purchase for item 10 = "))
item10_price = int(input("Enter Item10 Price = "))
item10_total = item10_qty * item10_price

# Discount check (sirf item 10 ke liye special condition)
item10_discount = 15
item10_after_discount = item10_total - (item10_total * item10_discount / 100)


total_bill = (item1_after_discount + item2_after_discount + item3_after_discount +
              item4_after_discount + item5_after_discount + item6_after_discount +
              item7_after_discount + item8_after_discount + item9_after_discount +
              item10_after_discount)

if total_bill > 10000:
    total_bill_discount = 15
# if total Bill amount is between 5000 and 10000 then you have to offer 10% of total bill amount
elif total_bill > 5000 and total_bill <= 10000:
    total_bill_discount = 10
else:
    total_bill_discount = 0

# D.P (bill-discount lagne ke baad ka amount, GST se pehle)
total_bill_after_discount = total_bill - (total_bill * total_bill_discount / 100)


ap_gst = total_bill * 10 / 100
dp_gst = total_bill_after_discount * 10 / 100

ap_total = total_bill + ap_gst
dp_total = total_bill_after_discount + dp_gst

ask = input("Do you Want Carry Bag (No/Yes) = ")
if ask == "Yes":
    carry_bag_charge = 10
    ap_total += carry_bag_charge
    dp_total += carry_bag_charge
else:
    print("Okay Good")

if gender == "Female":
    gift = "Cadbury"
elif gender == "Male":
    gift = "Leather Wallet"
else:
    gift = "Not Available"

print()
print("*" * 15, " D-Mart ", "*" * 15)
print(f"Name : {name}\t\t\tDate : 16/9/2022")
print("-" * 65)
print(f"{'Item Name':<12}{'Quantity':<12}{'Price':<10}{'Total':<10}{'After-Discount':<15}")

print(f"{item1_name:<12}{item1_qty:<12}{item1_price:<10}{item1_total:<10}{item1_after_discount:<15}")
print(f"{item2_name:<12}{item2_qty:<12}{item2_price:<10}{item2_total:<10}{item2_after_discount:<15}")
print(f"{item3_name:<12}{item3_qty:<12}{item3_price:<10}{item3_total:<10}{item3_after_discount:<15}")
print(f"{item4_name:<12}{item4_qty:<12}{item4_price:<10}{item4_total:<10}{item4_after_discount:<15}")
print(f"{item5_name:<12}{item5_qty:<12}{item5_price:<10}{item5_total:<10}{item5_after_discount:<15}")
print(f"{item6_name:<12}{item6_qty:<12}{item6_price:<10}{item6_total:<10}{item6_after_discount:<15}")
print(f"{item7_name:<12}{item7_qty:<12}{item7_price:<10}{item7_total:<10}{item7_after_discount:<15}")
print(f"{item8_name:<12}{item8_qty:<12}{item8_price:<10}{item8_total:<10}{item8_after_discount:<15}")
print(f"{item9_name:<12}{item9_qty:<12}{item9_price:<10}{item9_total:<10}{item9_after_discount:<15}")
print(f"{item10_name:<12}{item10_qty:<12}{item10_price:<10}{item10_total:<10}{item10_after_discount:<15}")

print("-" * 65)
print(f"{'':<30}{'A.P':<12}{'D.P':<12}")
print(f"{'':<30}{total_bill:<12}{total_bill_after_discount:<12}")
print(f"Gift :- {gift:<22}{'0.00':<12}{'0.00':<12}")
print(f"Carry Bag : {ask:<18}{carry_bag_charge:<12}{carry_bag_charge:<12}")
print(f"GST (10%):{'':<20}{ap_gst:<12}{dp_gst:<12}")

print("-" * 65)
print(f"{'':<30}{ap_total:<12}{dp_total:<12} Rs")
print()
print("Thank You")
print("To Visit")
print("D-Mart")
print("-" * 65)
