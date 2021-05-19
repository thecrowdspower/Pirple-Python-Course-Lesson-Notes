# Pirple List Lesson Homework

myUniqueList = []

myLeftovers = []

def addToList(newThing):
    if newThing in myUniqueList:
        # If newThing is in myUniqueList Add to myleftovers instead
        myLeftovers.append(newThing)
        return False
    else:
        myUniqueList.append(newThing)
        return True

# prints an empty list because nothing has been passed into the function.
print(myUniqueList)

# Function called  with newThing = "Dog"
addToList("Dog")

addToList("Cat")

print(myUniqueList)

print(addToList("Dog"))

print(myLeftovers)

print(addToList("Antelope"))

print(myUniqueList)

print(addToList("Antelope"))

print(myLeftovers)