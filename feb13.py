# 1. Total Revenue from Active Customers

def calculate_total_revenue(customers):
    total_revenue = 0.0

    for customer in customers:
        if customer["active"]:
            for purchase in customer["purchases"]:
                if purchase >= 100:
                    total_revenue += purchase * 1.10    

    return total_revenue



# 2. Total Discounted Price of Electronics

def calculate_discounted_total(products):
    total_price = 0.0

    for name, category, price in products:
        if category == "Electronics":
            total_price += price * 0.80 

    return total_price


# 3. Student Weighted Score Calculator

def calculate_total_updated_marks(students):
    total_marks = 0

    for student in students:
        marks = student["marks"]
        average = sum(marks) / len(marks)

        if average >= 60:
            updated_marks = [mark + 5 for mark in marks] 
            total_marks += sum(updated_marks)

    return total_marks


# Main Program

if __name__ == "__main__":

    # Problem 1 Data
    customers = [
        {"name": "A", "purchases": [50, 200, 300], "active": True},
        {"name": "B", "purchases": [500, 20], "active": False},
        {"name": "C", "purchases": [150, 250], "active": True}
    ]

    # Problem 2 Data
    products = [
        ("Laptop", "Electronics", 1000),
        ("Shirt", "Clothing", 50),
        ("Phone", "Electronics", 500)
    ]

    # Problem 3 Data
    students = [
        {"name": "A", "marks": [50, 60, 70]},
        {"name": "B", "marks": [30, 40]},
        {"name": "C", "marks": [80, 90]}
    ]

    # Outputs
    print("Total Revenue from Active Customers:", calculate_total_revenue(customers))
    print("Total Discounted Electronics Price:", calculate_discounted_total(products))
    print("Total Updated Marks:", calculate_total_updated_marks(students))




