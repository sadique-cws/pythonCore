# data types specify the type of data the can bee stored inside a variable. for example 
# num = 20

# here, 20 is an integer value assigned to the num variable. so data type of num variable is of the int class 

# python data type
# 1. numeric - (int, float, complex) this hold numeric values (2, -6.7, 1+2j)
# 2. string - (str)  this hold sequence of characters 
# 3. sequence 
    # a. list 
    # b. tuple 
    # c. range 
# sequence data type hold a collection of items.
# 4. Mapping - (dict) - a dictionary that hold data in key : value pair form.
# 5. boolean (bool) - it hold either True or False
# 6. set (set) - set data type using to hold a unique items.

# Note: in Python since Everything is an object. so data types are actually a classes. 

# ----------------------------------------
# Python Numbers: number data type can hold int, float, and complex values. 
# ----------------------------------------

# e.g 
# integers
num = 20
data = -2
# floating value 
result = 2.5
rank = -5
# complex no
a = 1 + 3j
# -----------------------------------------
# Python List : list is an ordered collection of items separated by commas enclosed within brackets. []
# -----------------------------------------
language = ["hindi","english","urdu","sanskrit","Bhojpuri"]

# access list items using indexing, negative indexing and slicing
print(language[0])#hindi

print(language[3])#sanskrit

print(language[-2]) #sanskrit

print(language[2:4]) #[urdu, sanskrit]

print(language[2:]) # ["urdu","sanskrit","bhojpuri"]

print(language[:3]) # ["hindi","english","urdu"]

print(language[::2]) # ["hindi","urdu","bhojpuri"]

# adding new item as last element
language.append("Maithili")

# adding new multiple items at the last of the list
language.extend(["spanish","greek"])

# --------------------------------------------------
# Python Tuple : is an ordered collection of items and it is immutable. enclosed within parenthesis separated by commas. 
# --------------------------------------------------

# e.g 
num = (2,3,5,3,5,7)

# ------------------------------------------------
# Python set data type : set is an unordered collection of unique items. enclosed within {} braces separated by comma
# ------------------------------------------------

# e.g
a  = {1,2,3,4,5,7,4} 
print(a) # {1,2,3,4,5,7}

# ----------------------------------------------
# python dictionary : is an ordered collections of items it store in key/ value pairs.
# ----------------------------------------------
# here, keys are unique that are associated with each value.
# e.g

capital = {
    "bihar":"patna",
    "jharkhand":"ranchi",
    "up":"lucknow"
}

print(capital["bihar"])

# --------------------------------------------
# python string: is a sequence of character enclosed using double, single, or even triple quotes.
# --------------------------------------------
# e.g
name = "rohit"
student = 'amit'
teacher = '''sadique'''