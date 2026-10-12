class mera_range:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_iterator(self)


class mera_iterator:
    
    def __init__(self, iterable):
        self.iterable = iterable
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start += 1
        return current

for i in mera_range(1, 10):
    print(i)