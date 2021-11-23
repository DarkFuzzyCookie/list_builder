import os


if not os.path.isdir('lists'):
    os.mkdir('lists')

class List:
    def __init__(self, _name=None, _items=None) -> None:
        self.name = _name
        self.items = []

        if _items is not None:
            self.items = _items
        if _name is not None:
            self.load_list()

    def defined(self) -> bool:
        if self.name is None:
            return False
        return True

    def empty(self) -> bool:
        if len(self.items):
            return False
        return True

    def add_item(self, item) -> bool:
        if item in self.items:
            return False

        self.items.append(item)
        return True

    def add_items(self) -> None:
        while True:
            item = input("New Item (x to exit): ")

            if item == 'x':
                break

            if not self.add_item(item):
                print("[ERROR] : Duplicate Entry!")
                continue

    def load_list(self) -> bool:
        if not os.path.isfile(f'lists/{self.name}.txt'):
            return False
        
        self.items = [] # clear the list prior
        with open(f'lists/{self.name}.txt', 'r') as file:
            for line in file.readlines():
                if line != '\n':
                    self.items.append(line[:-1])
        print(f"List Loaded : {len(self.items)} Elements")
        return True

    def save_list(self) -> bool:
        if not len(self.items) or self.name is None: # empty list
            return False

        with open(f'lists/{self.name}.txt', 'w+') as file:
            for item in self.items:
                file.write(f"{item}\n")
        return True

    def view_list(self) -> None:
        print(f"List {self.name}")
        print(f"{'-'*(5+len(self.name))}")
        if not len(self.items) or self.items is None:
            print("Empty!")
        else:
            for i, item in enumerate(self.items):
                print(f" {i+1}. {item}")
