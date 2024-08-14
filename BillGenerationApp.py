# Step 1: Setting Constants for Fruits Apple GST as 12% and Orange GST as 5%
APPLE_GST = 0.12 # 12% GST
ORANGE_GST = 0.05 # 5% GST

# Step 2: Enter buyer Name, Price and Orange per kg, and quantity
# of Apples and oranges in kg purchased by the buyer
buyer_name=(input("Enter Buyer Name: "))
apple_price_kg=int(input("Enter Apple price per kg: "))
apple_quantity_kg=float(input("Enter Apple Quantity in kg: "))
orange_price_kg=int(input("Enter orange price per kg: "))
orange_quantity_kg=float(input("Enter orange Quantity in kg: "))

# Step 3: Calculate TOtal price of Apple and Orange
total_price_apple = apple_price_kg * apple_quantity_kg
total_price_orange = orange_price_kg * orange_quantity_kg

# Step 4: Calculate the GST Amount for Apple and Orange
total_gst_apple = total_price_apple * APPLE_GST
total_gst_orange = total_price_orange * ORANGE_GST

# Step 5: Calculate the total billing amount for apple and oranges
# inclusive of GST
total_billing_apple = total_price_apple + total_gst_apple
total_billing_orange = total_price_orange + total_gst_orange

#Bill Generation App Part 2

# Step 6: Calculate total amount to be paid by the buyer and round it
total_amount = total_billing_apple + total_billing_orange
total_round_amount = round(total_amount)

# Print the bill
print(f'\nBuyer Name: {buyer_name}')
print(f"{'-' * 74}")
print(f"| {'Item Code':^10} | {'Price/Unit':^10} | {'#Unit':^5}",
      f"| {'Price':^5}  | {'GST':^10}  | {'Total w/GST':^10} |")
print(f"{'-' * 74}")
print(f"| {'Apple':^10} | {'Rs ' +str(apple_price_kg):^10} | {apple_quantity_kg:^5}",
      f"| {'Rs '+str(total_price_apple):^5} | {'Rs '+str(total_gst_apple):^10}",
      f"| {'Rs '+str(total_billing_apple):^10} |");
print(f"| {'Orange':^10} | {'Rs ' +str(orange_price_kg):^10} | {orange_quantity_kg:^5}",
      f"| {'Rs '+str(total_price_orange):^5} | {'Rs '+str(total_gst_orange):^10}",
      f"| {'Rs '+str(total_billing_orange):^10} |");
print(f"{'-' * 74}")
print(f"Total {' ' * 54} \u20B9 {total_amount:.2f}")
print(f"Total Round {' ' * 48} \u20B9 {total_round_amount:.2f}")
print(f"{'-' * 74}")