# tutorial: https://www.w3schools.com/python/python_dictionaries.asp

thisDict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(thisDict)  # prints the toString of thisDict, not its memory location

print(thisDict["brand"])  # prints 'Ford'

thisDict2 = {"color": "green", "brand": "Ford", "model": "Mustang", "year": 1964}
print(thisDict2)

thisdict = { #Duplicate values will overwrite existing values:
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict)) #print the number of items in the dictionary

thisdict = { #The values in dictionary items can be of any data type:
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}