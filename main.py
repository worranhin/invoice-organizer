import os
import csv

output_file_name = 'output.csv'  # 输出文件名 | the file name of the output csv file

# 日期格式化 | reformat the date
def dateFormatter(d):
    year = 2000 + int(d[0]) * 10 + int(d[1])
    month = int(d[2]) * 10 + int(d[3])
    day = int(d[4]) * 10 + int(d[5])
    formattedStr = '20' + d[0:2] + '-' + d[2:4] + '-' + d[4:6]
    return formattedStr

# 获取当前目录下的文件名列表，并整理发票信息 | get the file names, and arrange invoice information
file_list = os.listdir('.')
invoice_infos = []

for file in file_list:
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.pdf':
        date, name, price = file_name.split('-')
        date = dateFormatter(date)
        invoice_infos.append([date, name, price])

# 输出为 csv 文件 | output to csv file
with open(output_file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['date', 'item name', 'price'])
    csv_writer.writerows(invoice_infos)

print(f'{output_file_name} has been generated.')
