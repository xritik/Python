a = "Hello World!"
print(a)
print(a[1])
print(len(a))


# Looping through a String
for x in "Banana":
    print(x)

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Slicing
b = "Hello World"
print(b[2:5])
print(b[0:5])
print(b[:5])
print(b[2:])

print(b[-5:-2])

# Upper Case
a = "Hello World!"
print(a.upper())
print(a.lower())

# Remove WhiteSpace
a = " Hello, World! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(","))

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

# String Formate
age = 18
# print("My name is Ritik, I am " + age)  # incorrect code
print(f"My name is Ritik, I am {age}.")
print(f"I am {age} years old.")
print(f"I am {age:.2f} years old.")
print(f"I am {9 * 2} years old.")