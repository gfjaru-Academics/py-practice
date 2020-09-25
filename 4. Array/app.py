###
### Python Arrays and Operation in Arrays
###

# There are four collection datatype in Python
# List, Dict, Tuple and Sets

# List
This_is_a_list = ["Fubuki", "Mio", "Okayu", "Korone"]
# print(This_is_a_list)

# Data can be accesed by refereing index number
print(This_is_a_list[0])  ## show Fubuki

# Negative indexing, count from last record
print(This_is_a_list[-2])  ## show Okayu

# Range of Index
print(This_is_a_list[1:3]) ## only showing array record number 1 to 3

# Adding item?
This_is_a_list.append("Haachama")

# Remove (choose one)
This_is_a_list.pop() # Remove last one
del This_is_a_list[4] # Remove haachama
del This_is_a_list # remove list
This_is_a_list.clear() # Clear the entire list

# Copying list
fmok = This_is_a_list.copy()

# Joining 2 list
Gen_G = ["Fubuki", "Mio", "Okayu", "Korone"]
Gen_2 = ["Subaru", "Nakiri"]
smok = Gen_G + Gen_2

#####
## Difference between list, dict, tuple and sets

## Tuple is unchangeable once created
Tuple = ("this", "is", "a", "tuple")

## List is ordered and changeable
List = ["this", "is", "a", "list"]

## Dictionary is unordered, changeable, indexed
Dict = {
    "varA": "This",
    "varB": "is",
    "varC": "a",
    "varD": "Dictionary"
}

## Sets is unordered and unindexed
Sets = {"this", "is", "a", "sets"}
