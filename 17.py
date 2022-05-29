#Q-7 Sum values for each key in nested dictionary.
weapons = {'': None, 'sword': { 'steel': 151,
                                'sharpness': 100,
                                'age': 2,},
                                  
                     'arrow': {'steel': 120,
                               'sharpness': 205,
                               'age': 1,}}
                                 
sumValue1 = sum(d['sharpness'] for d in weapons.values() if d)
sumValue2 = sum(d['steel'] for d in weapons.values() if d)
  
print(sumValue1)
print(sumValue2)