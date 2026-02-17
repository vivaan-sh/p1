#A company wants to calculatew the total month salary pay out from  a list of employee salary .find the total sium of all the salaries
from functools import reduce

salaries = [25000, 30000, 40000, 35000, 50000]

total_salary = reduce(lambda x, y: x + y, salaries)

print("Total monthly salary payout:")
print(total_salary)

