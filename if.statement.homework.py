# Code checks for equality between function parameters using if statement
def EqChecker (x,y,z):
    if int(x) == int(y) or int(x) == int(z) or int(y) == int(z):
        return True
    else:
        return False

print(EqChecker(1,2,3))
print(EqChecker(1,1,2))
print(EqChecker(1,2,2))
print(EqChecker(2,2,2))

#Bonus

print(EqChecker(6,5,"5"))


 