#Input basic salary of an employee in BS and perform tasks on BS: HRA 24% of basic salary (BS) DA= 31% of basic salary (BS) Special allowance = 10% of basic salary (BS) if BS <= 10000 otherwise no allowance.
# Total salary=BS+ DA + HRA + special allowance Print basic salary (BS), DA, HRA, special allowance and total salary.

bs = float(input("enter the base salary"))
if(bs<=10000):
    totsal = bs + (0.24*bs)+(0.31*bs)
else:
    totsal = bs + (0.24*bs)+(0.31*bs) + (0.1*bs)
print("total salary is ",totsal)