#Q-9  Add new keys to a dictionary.
class my_dictionary(dict):
  
    # __init__ function
    def __init__(self):
        self = dict()
          
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
  
# Main Function
dict_obj = my_dictionary()
  
dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')
  
print(dict_obj)