from list import List


_list = List()

def menu() -> str:
    global _list

    print(f'{"-"*45}')
    print(f'Current List: {_list.name}\n')
    print(' 1. Change List')
    print(' 2. Add Items')
    print(' 3. Save List')
    print(' 4. View List')
    print(' x. Exit\n')
    inp = input('Choice: ')
    print(f'{"-"*45}')
    return inp


def main() -> None:
    global _list

    while True:
        choice = menu()
        
        if choice == '1':
            name = input("New Name: ")
            _list = List(_name=name)
        elif choice == '2':
            if not _list.defined():
                print("Please Select a List First!")
                continue
            _list.add_items()
        elif choice == '3':
            if not _list.defined():
                print("Please Select a List First!")
                continue
            if _list.save_list():
                print("List Saved!")
        elif choice == '4':
            if not _list.defined():
                print("Please Select a List First!")
                continue
            _list.view_list()
        elif choice == 'x':
            break
        else:
            print('Invalid Choice Entered!')
        

if __name__ == '__main__':
    main()
