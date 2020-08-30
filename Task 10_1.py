import csv

data = [
    ['Maria', 'Mariewna', '16'],
    ['Andrej', 'Andreewich', '41'],
    ['Vladimir', 'Vladimirowich', '24'],
    ['Anna', 'Annowna', '53'],
    ['Baby', 'Babykowich', '5']
]

my_file = open('people_data.csv', 'w')
my_file_writer = csv.writer(my_file)
my_file_writer.writerows(data)
my_file.close()

my_file = open('people_data.csv')
data_list = my_file.readlines()
for i in range(len(data_list)):
    data_list[i] = data_list[i].replace('\n','').split(',')

ages = [
    ['1-12: ', 0],
    ['13-18: ', 0],
    ['19-25: ', 0],
    ['26-40: ', 0],
    ['>40: ', 0]
]

for i in range(len(data_list)):
    if 1 <= int(data_list[i][2]) <= 12:
        ages[0][1] += 1
    elif 13 <= int(data_list[i][2]) <= 18:
        ages[1][1] += 1
    elif 19 <= int(data_list[i][2]) <= 25:
        ages[2][1] += 1
    elif 26 <= int(data_list[i][2]) <= 40:
        ages[3][1] += 1
    elif int(data_list[i][2]) > 40:
        ages[4][1] += 1

report = open('report.csv','w')
my_file_writer = csv.writer(report)
my_file_writer.writerow(['Age', 'Amount'])
my_file_writer.writerows(ages)
my_file.close()