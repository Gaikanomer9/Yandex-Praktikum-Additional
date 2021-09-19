
class OurList:
    def __init__(self, arr):
        self.arr = arr

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.arr):
            raise StopIteration
        return self.arr[self.index-1]

custom_list = OurList([1,2,3,4,5])

for custom_object in custom_list:
    print(custom_object)