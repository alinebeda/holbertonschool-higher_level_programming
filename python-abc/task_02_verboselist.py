#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            item = super().pop()
            print(f"Popped {item} from the list.")
        else:
            item = super().pop(index)
            print(f"Popped {item} from the list at index {index}.")
        return item

vl = VerboseList()
vl.append(1)
vl.append(2)
vl.extend([3, 4, 5])
vl.remove(3)
vl.pop()
vl.pop(0)
