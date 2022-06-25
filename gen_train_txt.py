import os
file_list = os.listdir('train')

print(file_list)

# writedata.py
f = open("train.txt", 'w')
for file in file_list:
    if file[-3:] == 'jpg':
        data = '/content/sht_test1/train/' + file + '\n'
        f.write(data)
f.close()

