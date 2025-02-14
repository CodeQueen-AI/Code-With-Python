#Dictionary
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
print(student.keys())

#Methods
#Keys()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
print(student.keys())  

#Values()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
print(student.values())  

#Items()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
print(student.items())  

#Get()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
print(student.get("grade"))  

#Update()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}

student.update({"height": "5'6", "city": "🏙️ Lahore"})
print(student)  

#Pop()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
age = student.pop("age")
print(age) 
print(student)  

#PopItems()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
student.popitem()
print(student)  

#Clear()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20,
    "grade": "A",
    "city": "🏙️ Karachi"
}
student.clear()
print(student)  

#copy()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20
}
new_student = student.copy()
print(new_student)  

#Del()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20
}
del student["age"]  
print(student)  

del student  # Puri dictionary delete ho jayegi  

#setdefault()
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20
}
result = student.setdefault("name", "Unknown")  
print(result) 
print(student)  

#Key does not exist
student = {
    "name": "👩‍🎓 Ayesha",
    "age": 20
}
result = student.setdefault("grade", "A")  
print(result)  

print(student)  

#formkeys(Iterable,value)
keys = ["name", "age", "grade"]
default_value = "Not available"
student = dict.fromkeys(keys, default_value)
print(student)  


