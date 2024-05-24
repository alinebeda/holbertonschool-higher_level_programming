#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):

        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        try:
            item = next(self.iterator)

            self.counter += 1
            return item
        except StopIteration:

            raise StopIteration

    def get_count(self):

        return self.counter

if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(items)

    for item in counted_iter:
        print(item)

    print("Number of items iterated:", counted_iter.get_count())
