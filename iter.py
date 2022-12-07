
class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.list = 0
        self.item = -1
        return self

    def __next__(self):
        self.item += 1
        if self.list >= len(self.nested_list) - 1 and self.item > len(self.nested_list[self.list]) - 1:
            raise StopIteration
        elif self.item > len(self.nested_list[self.list]) - 1:
            self.list += 1
            self.item = 0
            item = self.nested_list[self.list][self.item]
            return item
        else:
            item = self.nested_list[self.list][self.item]
            return item


class NewFlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.item = -1
        return self

    def __next__(self):
        self.item += 1
        if self.item > len(self.nested_list) - 1:
            raise StopIteration
        elif isinstance(self.nested_list[self.item], list):
            if self.nested_list[self.item]:
                iter_list = iter(self.nested_list[self.item])
                while next(iter_list) is not None:
                    return next(iter_list)
        else:
            return self.nested_list[self.item]
