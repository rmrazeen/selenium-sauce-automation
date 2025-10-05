#set function
print("\n set function")
def demonstrate_set_loop():
    _set = {10, 20, 30, 40, 50, 60, 70}
    # Sort the set to ensure a consistent order
    for item in sorted(_set):
        if item == 40:
            continue
        elif item == 70:
            break
        print(item)

#list function
print("\n list function")
def demonstrate_list_loop():
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in _list:
        if item == 4:
            continue
        elif item == 5:
            break
        print(item)

#dictionary function
print("\n dictionary function")
def demonstrate_dict_loop():
    _dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
    for key in _dict:
        if key == 'b' and _dict[key] == 100:
            continue
        elif key == 'd' and _dict[key] == 400:
            break
        print(f"{key}: {_dict[key]}")


# Call the functions to demonstrate their functionalitydemonstrate_set_loop()
print()  # Add spacing
demonstrate_list_loop()
print()  # Add spacing  
demonstrate_dict_loop()
print()  # Add spacing
demonstrate_set_loop()