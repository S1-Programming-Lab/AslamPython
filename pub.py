class publisher():
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("name:",self.pname)
class book(publisher):
    def __init(self,pname,bname,title):
        self.pname=pname
        self.bname=bname
        self.title=title
    def display(self):
        print("name:",self.pname)
        print("banme:",self.bname)
        print("title:",self.title)
class python(book):
    def __init__(self,pname,bname,title,page,price):
        self.pname=pname
        self.bname=bname
        self.title=title
        self.page=page
        self.price=price
    def display(self):
        print("Name:",self.pname)
        print("Bname:",self.bname)
        print("Title:",self.title)
        print("Page:",self.page)
        print("Price:",self.price)
n=input("Enter Publisher:")
b=input("Enter Author:")
t=input("Enter Title:")
p=input("Enter Pages:")
pr=input("Enter Price:")
obj=python(n,b,t,p,pr)
obj.display()
