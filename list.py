# Learn About Python Lists and How to Manipulate them

# A list is variable which contains more than one data value.
# The values in a list can be accessed using their index numbers which starts counting from 0
# Lists can take and group in any data type, together, including, strings, floats, integers, and even other lists.

# Structure of a list

#ListName = [value1, value2, value3, value4]

# Accessing List Values with their indexes

EmpList = ["Alabi", "Dominic", "Idris", "Rose", "Naomi","Malvin" ]

OldestEmp = EmpList[0]

print(OldestEmp)

MostValEmp = EmpList[1:5]

print(MostValEmp)

ResignedEmp = EmpList[0]

#print(ResignedEmp)

# Remove a list member

#EmpList.pop(0)

print(EmpList)

print(EmpList)

# Malvin is not an employee so remove him

EmpList.pop(-1)

print(EmpList)

# Job Roles

DigiMakter = EmpList[1]

print(DigiMakter)

CustomerRep = EmpList[4]

print(CustomerRep)

GraphicsDesigner = EmpList[2]

print(GraphicsDesigner)

SiteSupv = EmpList[3]

print(SiteSupv)

Resigned = EmpList[0]

print(Resigned)

EmpList.pop(0)

print(EmpList)

UpdatedEmpList = EmpList

print(UpdatedEmpList)