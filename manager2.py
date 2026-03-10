"""
Employee Salary Management System

This program uses inheritance to manage employee salary details.
The base class 'Employee' contains general employee information.
The derived class 'Manager' adds department and bonus information.
"""


class Employee:
    """
    Base class representing an employee.
    """

    def __init__(self, emp_id, name, base_salary):
        """
        Constructor to initialize employee attributes.

        Args:
            emp_id (int): Employee ID
            name (str): Employee name
            base_salary (float): Monthly salary
        """
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_employee(self):
        """
        Displays employee details.
        """
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Base Salary:", self.base_salary)

    def annual_salary(self):
        """
        Calculates annual salary.

        Returns:
            float: Yearly salary
        """
        return self.base_salary * 12


class Manager(Employee):
    """
    Derived class representing a manager.
    Inherits from Employee and adds department and bonus.
    """

    def __init__(self, emp_id, name, base_salary, department, bonus):
        """
        Constructor to initialize manager attributes.
        """
        super().__init__(emp_id, name, base_salary)
        self.department = department
        self.bonus = bonus

    def total_salary(self):
        """
        Calculates total annual salary including bonus.

        Returns:
            float: Total salary
        """
        return self.annual_salary() + self.bonus

    def display_manager(self):
        """
        Displays all manager details including total salary.
        """
        self.display_employee()
        print("Department:", self.department)
        print("Bonus:", self.bonus)
        print("Total Annual Salary:", self.total_salary())
        print("---------------------------")


# Creating manager objects
manager1 = Manager(201, "Rahul", 50000, "IT", 100000)
manager2 = Manager(202, "Priya", 60000, "HR", 120000)
manager3 = Manager(203, "Amit", 55000, "Finance", 90000)

# Storing objects in a list
managers = [manager1, manager2, manager3]

# Display manager details
print("Manager Details\n")

for manager in managers:
    manager.display_manager()