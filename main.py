from iter import FlatIterator, NewFlatIterator


def flat_generator(nested_list):
    for list in nested_list:
        for item in list:
            yield item


def new_flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            generated_list = new_flat_generator(item)
            for i in generated_list:
                yield i
        else:
            yield item


nested_list = [
    1,
    [],
    ['a', 'b', 'c', []],
    ['d', 'e', ['a', '1', [9, 8, 7]], 'f', 'h', False],
    [1, 2, None],
]


new_list = [i for i in new_flat_generator(nested_list)]
print(new_list)

for item in NewFlatIterator(nested_list):
    print(item)