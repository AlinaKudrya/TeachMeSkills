dictionary = {'test':'test_value', 'europe':'eur', 'dollar':'usd', 'ruble':'rub'}
keys = list(dictionary.keys())
new_key = 0

print('FOR')
for new_key in range(len(dictionary)):
    key = keys[new_key]+str(len(keys[new_key]))
    value = dictionary[keys[new_key]]
    dictionary.pop(keys[new_key])
    dictionary.update({key: value})
print(dictionary, '\n')

#############

print('WHILE')
dictionary = {'test':'test_value', 'europe':'eur', 'dollar':'usd', 'ruble':'rub'}
while new_key != len(dictionary):
    key = keys[new_key]+str(len(keys[new_key]))
    value = dictionary[keys[new_key]]
    dictionary.pop(keys[new_key])
    dictionary.update({key : value})
    new_key += 1

print(dictionary)