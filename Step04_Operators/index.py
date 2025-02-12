# Arithematic Operators
a = 10 + 5  #15
print(a)  
b = 10 - 5   #5
print(b) 
c = 10 * 5   #50
print(c)  
d = 10 / 2   #5.0
print(d) 
e = 10 % 3   #1
print(e) 
f = 10 ** 2  #100
print(f) 
g = 10 // 3  #3
print(g)

#Comparison operators
x = 5 > 3   # Greater than (True)
print(x)
y = 5 < 3   # Less than (false)
print(y)
z = 5 == 5  # Equal to (True)
print(z)
w = 5 != 3  # Not equal to (True)
print(w)
p = 5 >= 5  # Greater than or equal to (True)
print(p)
q = 5 <= 10 # Less than or equal to (True)
print(q)

#Logical Operators
a = (5 > 3) and (10 > 5)  # True
print(a)
b = (5 > 10) or (10 > 5)  # True
print(b)
c = not(5 > 3)            # False
print(c)

#Assignment Operators
x = 10  
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 2  # x = x / 2
x %= 4  # x = x % 4
x **= 3 # x = x ** 3
print(x)

#Bitwise Operators
a = 5 & 3  # AND
b = 5 | 3  # OR
c = 5 ^ 3  # XOR
d = ~5     # NOT
e = 5 << 1 # Left Shift
f = 5 >> 1 # Right Shift
print(a, b, c, d, e, f)

#Memebership Operators
my_list = [1, 2, 3]
print(2 in my_list)   # True (2 is in the list)
print(5 not in my_list) # True (5 is NOT in the list)

#Identity Operators
a = [1, 2, 3]  
b = a  
print(a is b)     # True (Same object)
print(a is not b) # False (Not different objects)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True (Same values)
print(x is y)  # False (Different objects)

