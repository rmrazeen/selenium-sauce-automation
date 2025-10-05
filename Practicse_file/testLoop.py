#list
print("Demonstrating break continue in a loop:")
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in _list:
    if item == 4:
        continue
    elif item == 5:
        break
    print(item)
print()  # Add spacing
#set
print("Demonstrating continue and break in a set:")
_set = {10, 20, 30, 40, 50, 60, 70}
for item in _set:
    if item == 40:
        continue
    elif item == 70:
        break
    print(item)  
print()  # Add spacing
#disctionary
print("Demonstrating break and continue in a dictionary:")
_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
for key in _dict:
    if key == 'b' and _dict[key] == 100:
        continue
    elif key == 'd' and _dict[key] == 400:
        break
    print(f"{key}: {_dict[key]}")

print()  # Add spacing
#string 
print("Demonstrating break and continue in a string:")
_string = "Python"
for char in _string:
    if char == 'h':
        continue
    elif char == 'o':
        break
    print(char)
print()  # Add spacing
#tuple  
print("Demonstrating break and continue in a tuple:")
_tuple = (1, 2, 3, 4, 5, 6)
for item in _tuple:
    if item == 3:
        continue
    elif item == 5:
        break
    print(item)
print()  # Add spacing      

#range
print("Demonstrating break and continue in a range:")
for num in range(1, 10):
    if num == 6:
        continue
    elif num == 8:
        break
    print(num)
print()  # Add spacing

#nested loop
print("Demonstrating break and continue in a nested loop:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            continue
        elif i == 2 and j == 2:
            break
        print(f"i: {i}, j: {j}")        
print()  # Add spacing

#while
