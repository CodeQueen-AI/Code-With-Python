#Access Elements in Tuple
#Indexing
my_tuple = ("apple", "banana", "cherry", "date")
print(my_tuple[0])  
print(my_tuple[2])  

#Negative Indexing
my_tuple = ("apple", "banana", "cherry", "date")
print(my_tuple[-1])
print(my_tuple[-2])  

#Slicing
my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
print(my_tuple[1:4])  
print(my_tuple[:3])  
print(my_tuple[2:]) 

#Immutable
my_tuple = (1, 2, 3, 4)
my_tuple[2] = 10  

#Operations in Tuple
#Concatenating Tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple) 

#Single Element
single_tuple = (5,)  
not_a_tuple = (5)   
print(type(single_tuple)) 
print(type(not_a_tuple))   

#Convert Tuple to List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)  
my_list.append(4)        
print(my_list)          

#Tuple Unpacking
my_tuple = ("apple", "banana", "cherry")
a, b, c = my_tuple
print(a) 
print(b) 
print(c)  

