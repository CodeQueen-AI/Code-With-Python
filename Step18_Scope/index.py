#Local Scope
def my_function():
    x = 10
    print(x) 

my_function()
print(x)  


#Enclosing Scope
def outer_function():
    y = 20  
    def inner_function():
        print(y)  
    inner_function()
outer_function()


#Global Scope
z = 30
def my_function():
    print(z) 
my_function()
print(z)  


#Built-in Scope
print(len("Hello")) 

#local Variable
def my_function():
    x = 10  
    print(x)  

my_function()
print(x)  


#Global Variable
y = 50 
def my_function():
    global y
    y = 100
    print(y)  

my_function()
print(y) 