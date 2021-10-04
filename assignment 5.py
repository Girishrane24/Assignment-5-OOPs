class girish:
    def power(self,x,n):
        return pow(x,n)
x,n = map(int,input().split())
obj1 = girish()
print(obj1.power(x,n))