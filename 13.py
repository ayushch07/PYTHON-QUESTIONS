#Q-3 Merging two Dictionaries.
def Merge(dict1, dict2):
    return(dict2.update(dict1))
     
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This return None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2)