#strings
a = "Hello"
print(a)
b = "Hello, World!"
print(b[2:5])
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))