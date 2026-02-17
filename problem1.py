# A bank wants to identify costumers with minimum bank balance of 100000 rs to offer them a premium acc filter out those who qualify for the premium acc 
customers = {
    "Amit": 85000,
    "Priya": 150000,
    "Rahul": 99000,
    "Sneha": 200000,
    "Vikram": 120000
}

premium_customers = dict(filter(lambda item: item[1] >= 100000, customers.items()))

print("Customers eligible for Premium Account:")
print(premium_customers)

