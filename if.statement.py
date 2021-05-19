# If statements are used to make something happen only when a condition is met or not met.
"""
Structure of an if statement:

if condition:
    Action
condition is the situation that must be True or False before which a specific Action can take place.

"""

# Let's create an Instagram Like Counter if statement

# Create variables

click = False
Like = 0
click = True

if click == True:
    Like = Like + 1
    click = False

#print(Like)

# Create Code to detect and regulate the temperature of a room usinf if statement

Temp = 40 # Hottest temperature in Nigeria
Thermo = 50 # Standard themostat value

if Temp > 30: # Condition for Thermostat to regulate temperature
    Thermo = Thermo - 34 # Action to take if condition is met.
    #which is to bring room temperature down to 16 degree celsius when high temperature above 30 degrees is detected

print(Thermo) # Thermostat reading if condition is met