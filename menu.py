print("Welcome to myCalc")

num1 = input("Please type a number: ")
num2 = input("Please type another number: ")

#parse string to floats
float1=float(num1)
float2=float(num2)

#math operations
print("Sum: ", float1+float2)
print("Dif: ", float1-float2)
print("Pro: ", float1*float2)
print("Quo: ", float1/float2)
#Floor Division results with no remainder
print("Floor Division ",float1%float2)

# define a function
def say_hello():
    print("Hello from a function")

def perform_sum(num1,num2):
    res=(num1+num2)
    print(res)
    return res #return the result from the function

# execute the function
say_hello()
result=perform_sum(21,21) #catch the return from a function
print("Result from the fn", result)

