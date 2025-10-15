class stack:
    def __init__(self,term):
        self.term=term
        self.li=[]

    def push(self,val):
        if(len(self.li)==self.term):
            print("stack overflow")
        else:
            self.li.append(val)

    def pop(self):
        if len(self.li)>0:
            return self.li.pop()
        else:
            return None
        
    def peek(self):
        if len(self.li)>0:
            return self.li[-1]
        else:
            return None
    
    def display(self):
        print(self.li)

class queue:
    i=0
    def __init__(self,term):
        self.term=term
        self.li=[]
        self.i=0

    def enqueue(self,val):
        if(len(self.li)==self.term):
            print("stack overflow")
        else:
            self.li.append(val)

    def dequeue(self):
        if(self.li):
            n= self.li.pop(self.i)
            #self.i=(self.i)+1
            return n
        else:
            return None
        
    def display(self):
        for k in range(self.i,len(self.li)):
            print(self.li[k],end=" ")
        

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insertend(self,val):
        newnode=node(val)
        if self.head==None:
            self.head=newnode
            print("element inserted \n")
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=newnode
            print("element inserted \n")

    def display(self):
        if(self.head==None):
            print("empty list")
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next

            

s1=stack(5)     
# while(1):
#     print("enter 1 to push 2 to pop 3 to display 4 to peek \n")
#     c=int(input("enter your choice "))
#     if(c==1):
#         n=int(input("what you want to push "))
#         s1.push(n)
#     elif(c==2):
#         n=s1.pop()
#         print("popped element is ",n)
#     elif(c==3):
#         s1.display()
#     elif(c==4):
#         x=s1.peek()
#         print(x)

# q1=queue(5)
# while(1):
#     print("enter 1 to enqueue 2 to dequeue 3 to display  \n")
#     c=int(input("enter your choice "))
#     if(c==1):
#         n=int(input("what you want to push "))
#         q1.enqueue(n)
#     elif(c==2):
#         n=q1.dequeue()
#         print("popped element is ",n)
#     elif(c==3):
#         q1.display()
#     elif(c==4):
#         x=s1.peek()
#         print(x)

l1=linkedlist()
while(1):
    print("enter 1 to insert at end 2 to dequeue 3 to display  \n")
    c=int(input("enter your choice "))
    if(c==1):
        n=int(input("what you want to insert at end "))
        l1.insertend(n)
    elif(c==2):
        print("nothing")
    elif(c==3):
        l1.display()

       



