
customer_29876 = {
 "first name": "David",
 "last name": "Elliott",
 "address": "4803 Wellesley St.",
 "discounts": ["brother in law", "volume", "loyalty"],
}
discount_amount = 0 

if "brother in law" in customer_29876["discounts"]:
     discount_amount += .30
if "loyalty" in customer_29876["discounts"]:
     discount_amount += .15
if "volume" in customer_29876["discounts"]:
     discount_amount += .10

print(discount_amount)
