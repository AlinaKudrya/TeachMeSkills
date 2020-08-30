numbers = [1, 2, 0, 5, 32, 1, 0, 1, 5, 6]
count = ''
count_int = 0


for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        count += '1'
    else:
        count += '0'

count = count.split('0')

for i in count:
    if i.count('1') != 0:
        count_int += 1

print(count_int)

#print(parts)
#print(len(parts.split('0')))