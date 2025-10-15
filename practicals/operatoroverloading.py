class fraction:
    def __init__(self,num,dem):
        self.num=num
        self.dem=dem

    def __add__(self,other):
        newnum=((self.num)*(other.dem)) + ((self.dem)*(other.num))
        newdem=(self.dem)*(other.dem)
        return newnum,newdem
    
    def __sub__(self,other):
        newnum=((self.num)*(other.dem)) - ((self.dem)*(other.num))
        newdem=(self.dem)*(other.dem)
        return newnum,newdem
    
f1=fraction(3,4)
f2=fraction(2,5)
print(f1+f2)
print(f1-f2)