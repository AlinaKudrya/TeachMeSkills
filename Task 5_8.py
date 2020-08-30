entered_string = input().split(' ')[::-1]
new_string = ''

for i in range(len(entered_string)):
    new_string += entered_string[i] + ' '

print(new_string)