# Question 1
msg :str = "Hello Google"
print (msg)

# Question 2
msg1 :str = "Hello Ali"
print (msg1)

msg1 = "Hello Hassan"
print (msg1)

# Question 3
pname :str = "Asad"
print (f'"Hello {pname} , whould you like to earn money?"')


# Question 4
name2 :str = "Abu bakar"
print (name2.upper())
print (name2.lower())
print (name2.title())

# Question 5
print ('Quiad-e-Azam said :" I do not believe in taking the right decision, I take a decision and make it right."')

# Question 6
Famous_person :str = "Quiad-e-Azam"
quets :str = f'{Famous_person} said :" Expect the best, prepare for the worst."'
print (quets)

# Question 7
name : str = "\n\tM Anas\n\t"

print ("this is orignal state : ",repr(name))

# using rstrip() method

print("By rstrip () : ",repr(name.rstrip()))

# using lstrip() method 

print("By lstrip () : ",repr(name.lstrip()))

# using strip() method 

print("By strip () : ",repr(name.strip()))

# Question no 8
x : int = 2
y : int = 3
z : int = 4
print("Sum of X,Y,Z = ",x + y + z)

# Question no 9
a : int = 3
b : int = 4
print(f"Before swap : a = {a} , b = {b}")
a , b = b , a
print(f"After swap : a = {a} , b = {b}")

# Question no 10
fav_color :str = "Light_Red"
print(fav_color)
new_color : str = fav_color
print(new_color)

# Question no 11
pet_name :str = "Tomy"
pet_name = "Buldog"
print (pet_name)

# Question no 11
Day : str = "Sunshine"
print(Day)
# print(day) 
# Eror =   print(day)
#           ^^^
# NameError: name 'day' is not defined. Did you mean: 'Day'?

# Question no 13
score : int = 100
print(score)
score = 110
print (score)

# Question no 14
city :str 
city = "Jaddah"
print (city)

# Question no 15
text :str = "python programming"
text = text.title()
print ("Title case : ",text)

# Question no 16
text = text.upper()
print("Upper case : ",text)

# Question no 17
print("Lower case : ",text.lower())

# Question no 18
temprature : int = 25
print(f"\"Crrunt temprature is {temprature} degrees\"")

# Question no 19
poem : str = '''\nUnderneath the starlit sky so clear,
Dreams take flight and wander near,
In the quiet, whispers sing,
Of hopes and wishes, fragile things.'''
print (poem)