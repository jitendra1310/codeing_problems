import csv

data = open('/var/www/html/udemy/python/csv and pdf/example.csv',encoding='utf-8')
csv_data = csv.reader(data)
data_line = list(csv_data)
all_email = []
full_name = []
for line in data_line[1:5]:
    all_email.append(line[3])
    full_name.append(line[1]+' '+line[2])

print(all_email) 

#Save File In CSV
file_to_output = open('/var/www/html/udemy/python/csv and pdf/file_to_output.csv',mode='w',newline='' ,encoding='utf-8')
csv_witer = csv.writer(file_to_output, delimiter=',')
csv_witer.writerow(['a','b','c'])
csv_witer.writerows([['1','2','3'],['4','5','6']])

#close the fileile
file_to_output.close()


#Add New Row On existing csv file
f = open('/var/www/html/udemy/python/csv and pdf/file_to_output.csv',mode='a',newline='' ,encoding='utf-8')
csv_witer = csv.writer(f, delimiter=',')
csv_witer.writerow(['7','8','9'])
f.close()
