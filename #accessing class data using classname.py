#accessing class data using classname

class Demo:
    count=0
    def increment(self):
        Demo.count=Demo.count+1
        print('No of object created=',Demo.count)
    def total(self):
        print('Total no of objects creagted=',Demo.count)

x=Demo()
x.increment()
y=Demo()
y.increment()
z=Demo()
z.increment()
z.total
