customers = [
    ("Krisha", 85000),
    ("Prapti", 150000),
    ("Rishita", 99000),
    ("Diya", 200000),
    ("Mehek", 120000)
]

premium_customers = [customer for customer in customers if customer[1] >= 100000]

print("Customers eligible for Premium Account:")
print(premium_customers)
