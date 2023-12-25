# Creating a tuple
years = (2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010)

#Accessing first element of a tuple
print(years[0])

#Accessing last element of a tuple
print(years[-1])

if 2000 in print:
  print("The year 2000 is inside of this tuple")
else:
  print("The year 2000 is not inside of this tuple")

#Adding an element to a tuple
years.append(2011)
years.remove(2011)

#Looping through a tuple

for i in range(len(years)):
  print(years[i])

for x in years:
  print(x)

# Tuple Methods
years.count(2000)
years.index(2005)

  
