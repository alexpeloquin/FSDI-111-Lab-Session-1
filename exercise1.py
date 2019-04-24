#add elements to an array
#animals.append("Lion")
#animals.append("Tiger")
#animals.append("Bear")

#print("Animals in the array", len(animals))
#print(animals[0])

# for loop over the array
# for each animal within animals print the value
#for animal in animals:
#    print(animal)

'''
Functionality:
    -present a menu
    -exit the app with the X
    -allow the user to add animals
    -allow the user to see how many animals there are
    -allow the user to see the list of animals 
'''

#Create an Array
animals=[]

def menu():
    print("\n\n\n\n")
    print("*** Welcome to XYZ System ***")
    print("-"*20)
    print("1 - Add new animal")
    print("2 - List the animals")
    print("3 - Count the animals")
    print("4 - Print the list in order(sorted)")
    print("X - Close the system")
    opc = input("Please choose an action: ")
    return opc

def create_new():
    new_animal=input("What is the animal you would like to add? ")
    animals.append(new_animal)
    print("New",new_animal,"saved!")
    input("Press enter to continue")

def print_list():
    for animal in animals:
        print(animal)

def count_list():
    print("There are:",len(animals),"animals in the system")

def sort_list():
    sorted_array = sorted(animals) #sort ABC
    for animal in sorted_array:
        print(animal)
    
#Start the app
selection = "animals"
while selection !="x":
    selection = menu()
    if(selection=="1"):
        create_new()
    elif(selection=="2"):
        print("The following animals in the system are:")
        print_list()
    elif(selection=="3"):
        count_list()
    elif(selection=="4"):
        sort_list()
    else:
        print("** Incorrect option, try again")
       
print("You selected", selection)

#this line its outside the while loop
print("Good bye")
