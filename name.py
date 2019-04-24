print("****Hello****")
name=input("Please input your name: ")
print("Your name is:",name)

name_length=len(name) #Get the length of a variable or array)
print("Your name has ", name_length,"letters")
print("The first letter is:" , name[0]) #read a character from the start of string
print("In Uppers: ",name.upper()) #convert to upper case
print(name.replace("l","w")) #replace l with an w
contains = "w" in name # does the string contain an X
print("Your name contain a X", contains)

print("**************")
animal = input("What kind of pet do you have? ")
if("CAT" in animal.upper()):
    print("So its a cat")
elif("DOG" in animal.upper()):
    print("So a dog")
else:
    print("Another type of animal")





print("**************")

