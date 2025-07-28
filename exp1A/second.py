#Accept Employee Code( Ec), monthly salary (sal). Calculate 21.5% special allowance (SPL) on salary. Calculate total monthly salary (SAL+SPL) and annual salary of the employee.

Ec = input("Enter the employee code ")
sal = float(input("Enter the salary "))
spl = 0.215*sal
totsal = sal+spl
print("Annual salary is ",totsal)