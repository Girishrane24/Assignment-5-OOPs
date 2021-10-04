class girish:
    def __init__(self,x,n):
        self.x = x
        self.n = n
        self.ans = 0
    def power(self):
        return pow(self.x,self.n)
x,n = map(int,input().split())
obj1 = girish(x,n)
print(obj1.power())
