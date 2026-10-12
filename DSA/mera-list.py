import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a c type arr with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if 0<=index<=self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range' #raise IndexError('Index out of range')


    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)

        # append
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        # Create a new array with new capacity.
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # Copy the content from A to B.
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def find(self, val):
        for i in range(self.n):
            if self.A[i] == val:
                return i
        return 'ValueError - Not in the list'

    def insert(self, pos, val):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] = val
        self.n += 1

    def remove(self, val):
        pos = self.find(val)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    def __delitem__(self, pos):
        if 0<=pos<=self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1

    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n-1

    def clear(self):
        self.n = 0
        self.size = 1

    def __make_array(self, capacity):
        # Creates a C-type array with size capacity.
        return (capacity*ctypes.py_object)()

L = MeraList()
L.append(1)
L.append(2)
L.append(3)
print(L)
print(L[0])
print(L[1])
L.insert(0, 0)
del L[2]
L.remove(3)
print(L)
