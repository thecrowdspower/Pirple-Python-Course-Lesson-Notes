# Function is way to define certain things or actions you want to do over and over again.
# With a Function you will never have to repeat those Actions every time you want to perform them.
# You can simply perform the action by calling or reusing the function.
# So you create a Function once, and use it many times.

"""
Structure of Functions in Python

def functionName (Input):
  Action to be performed
  Return Output

 """ 

 # Time to Create my First Function

 # This function will increase an input variable by 1
"""
def addOne(Number):
  Number += 1
  return Number

var = 0
var1 = addOne(var)
print(var1)

var2 = addOne(var1)
print(var2)    
var3 = addOne(5.4)
print(var3)

var4 = addOne(3.4 + 4.8)
print(var4)
"""

# Another Function that adds two inputs and return the value.

def AddOneAddTwo (num1, num2):
    Output = num1 + 1
    Output += num2 + 2
    return Output

Sum = AddOneAddTwo (1,2)

print(Sum)
