#Although arrays are pre-defined in Python in the form of lists, we can implement our own arrays.
#Here, we will implement our own array with some common methods such as access, push, pop, insert, delete

class my_array():
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        print(self.data.values())
        return str(self.__dict__)
    
    #push
    def push(self, item):
        self.length+=1
        self.data[self.length-1]=item

    #insert
    def insert(self, index, item):
        self.length += 1
        for i in range(index, self.length-1, -1):
            self.data[i]=self.data[i-1]
        self.data[index]=item

    #delete
    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length-=1

    #pop
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return last_item
    
    #get
    def get(self, index):
        return self.data[index]
    
arr = my_array()
arr.push(4)
arr.push(1)
arr.push(0)
arr.push(2)
arr.push(9)
arr.push(6)
arr.push(8)
arr.push(7)
arr.push(5)
print(arr)

arr.insert(3,10)
print(arr)

print(arr.get(5))
print(arr.pop())
arr.delete(2)
print(arr)