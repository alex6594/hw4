class FlatIterator:
    def __init__(self, list: list):
        self.list = list

    def __iter__(self):
        self.iteration_list = iter(self.list)
        self.cursor = -1
        self.new_list = []
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            self.cursor = 0
            self.new_list = None
            while not self.new_list:
                self.new_list = next(self.iteration_list)
        return self.new_list[self.cursor]


def flat_generator(nested_list_file):
    for list in nested_list_file:
        for element in list:
            yield element


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    print('Начало итерации')
    for item in FlatIterator(nested_list):
        print(item)
    print(20 * '_')
    print('Итерация завершена')
    print(20 * '_')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print(20 * '_')
    print('Вывел комперхеншн')
    print(20 * '_')
    for item in flat_generator(nested_list):
        print(item)
    print(20 * '_')
    print('Вывел генератор')
    print(20 * '_')
