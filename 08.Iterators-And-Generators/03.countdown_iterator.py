class countdown_iterator:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        while self.num >= 0:
            current_num = self.num
            self.num -= 1
            return current_num
        raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
