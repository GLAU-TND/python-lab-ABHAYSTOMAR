class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        print(self.v)

def XYZ(a,b):
    c=a+b
    if c<150:
        raise MyException('Custom Exception ocurred')
    else:
        return c
a=int(input())
b=int(input())
print(XYZ(a,b))