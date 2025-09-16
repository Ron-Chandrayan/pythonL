'''Exception Handling:
1. Built in exception
2. User defined exception  '''

#Built in exception
def avg(list):
  tot = 0
  for x in list:
    tot+=x
  avg = tot/len(list)
  return tot,avg

try:
  t,a = avg(["a","b"])
  print('Total={}, Average = {}'.format(t,a))
except TypeError:
  print('Type Error , please provide numbers')
except ZeroDivisionError:
  print('ZeroDivisionError, please do not give empty list')

#User defined exception
class MyException(Exception):
  def __init__(self,arg):
    self.arg = arg

def check(dict):
  for k,v in dict.items():
    print('Name ={} Balance ={:10.2f}'.format(k,v))
    if(v<2000.00):
      raise MyException('Balance amount is less in the account of '+ k)

bank = {'Raj': 5000.000, 'Vani':8900.50,'Ajay':199.00,'Naresh':3000.00}

# handle the myexception
try:
  check(bank)
except MyException as me:
  print(me)

