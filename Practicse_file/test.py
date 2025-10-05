""" user_input = int(input("Enter a Number: "))
print(f"{user_input}*2 = {user_input*2}") # f is used for formatting the string """

x = "hello"
print(x.capitalize())  # Hello
print(x.upper())  # HELLO 
# start:end:step
x = "python"
print(x[1:4])     # Output: 'yth'
print(x[:3])      # Output: 'pyt'
print(x[::2])     # Output: 'pto' (every second character)
print(x[::-1])    # Output: 'nohtyp' (reversed string)
#set
a = {"red", "blue", "green","red"}
print(a)  # Output: {'red', 'blue', 'green'}
a.add("yellow")
print(a)  # Output: {'red', 'blue', 'green', 'yellow'}
#list
b = [1, 2, 3, 4, 5]
b.append(6)
print(b)  # Output: [1, 2, 3, 4, 5, 6]
#tuple
c = (1, 2, 3, 4, 5, 5)
print(c)  # Output: (1, 2, 3)
#dictionary
d = {"name": "Alice", "age": 30}
print(d)  # Output: {'name': 'Alice', 'age': 30}    