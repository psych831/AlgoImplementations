class stack:
    def __init__(self):
        self.MAX_SIZE = 100
        self.a = []
        self.length = -1
    
    def push(self,x):
        if self.length >= self.MAX_SIZE:
            print('Cannot Add. Stack full')
        else:
            self.length+= 1
            self.a.append(x)
            print('Push Successful')
            

    def top(self):
        if self.length == -1:
            print('Empty Stack')
        else:
            print(self.a[self.length])

    def isEmpty(self):
        if self.length == -1:
            print('Empty')
        else:
            print('Not Empty')


    def pop(self):
        if self.length == -1:
            print('No elements')
        else:
            self.a.pop()
            self.length-=1
            print('Pop Successful')



x = stack()
x.push(5)
x.push(12)
x.push(4)
x.push(7)
x.top()
x.pop()
x.top()
x.pop()
x.pop()
x.pop()
x.pop()
x.pop()