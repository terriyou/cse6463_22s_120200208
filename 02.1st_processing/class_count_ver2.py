import argparse
import os

parser = argparse.ArgumentParser(description='count classes with dir name and class total cnt')
parser.add_argument('dir_name',  type=str, help='dir name within labeled txt files')
parser.add_argument('class_cnt', type=int, help='number of classes')

args = parser.parse_args()

#print(args.dir_name)
#print(args.class_cnt)

def file_path_gen(path):
    file_path_list = []
    for (root, _, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_list.append(file_path)

    return file_path_list

file_paths = file_path_gen(args.dir_name)

classes_room = [[0] for i in range(args.class_cnt)]

for file in file_paths:
    f = open(file, 'r')
    lines = f.readlines()
    for line in lines:
        idx = int(line.split(' ')[0])
        classes_room[idx][0] = classes_room[idx][0] + 1
    f.close()
    
f = open('class_cnt_1.txt','w')
for classes_room_one in classes_room:
    f.write(str(classes_room_one))
    f.write('\n')
f.close()
    
print(classes_room)













"""


"""
