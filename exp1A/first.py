#Accept Product Code (Pc), Quantity (Qty) and Price of product (Pr). Calculate total cost of the product, 12.5% #discount on total cost and net price to be paid after discount

Pc=input("Enter product code ")
qty=int(input("Enter the quantity "))
Pr=float(input("Enter price of the product "))
totcost = (Pr*qty)
discost = totcost - (0.125*totcost)
print("total cost is ",totcost)
print("Discounted price is ",discost)