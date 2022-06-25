import glob
import random
import os
import shutil

# Get all paths to your images files and text files
PATH = 'obj/'
img_paths = glob.glob(PATH+'*.jpg')
txt_paths = glob.glob(PATH+'*.txt')

# Calculate number of files for training, validation
data_size = len(img_paths)
train_size = int(data_size * 0.7)
val_size = int(data_size * 0.2)
test_size = data_size - (train_size + val_size)

# Shuffle two list
img_txt = list(zip(img_paths, txt_paths))
random.seed(43)
random.shuffle(img_txt)
img_paths, txt_paths = zip(*img_txt)

val_size_split = train_size + val_size

# Now split them
train_img_paths = img_paths[:train_size]
train_txt_paths = txt_paths[:train_size]

valid_img_paths = img_paths[train_size:val_size_split]
valid_txt_paths = txt_paths[train_size:val_size_split]

test_img_paths = img_paths[val_size_split:]
test_txt_paths = txt_paths[val_size_split:]

f = open('train.txt', 'w')
for train_img_path in train_img_paths:
    f.write('/content/cse6463_22s_120200208/')
    f.write(train_img_path.replace("\\","/"))
    f.write('\n')
f.close()

f = open('valid.txt', 'w')
for valid_img_path in valid_img_paths:
    f.write('/content/cse6463_22s_120200208/')
    f.write(train_img_path.replace("\\","/"))
    f.write('\n')
f.close()

f = open('test.txt', 'w')
for test_img_path in test_img_paths:
    f.write('/content/cse6463_22s_120200208/')
    f.write(train_img_path.replace("\\","/"))
    f.write('\n')
f.close()


"""
# Move them to train, valid folders
train_folder = PATH+'train/' 
valid_folder = PATH+'valid/'
os.mkdir(train_folder)
os.mkdir(valid_folder)


def move(paths, folder):
    for p in paths:
        shutil.move(p, folder)

move(train_img_paths, train_folder)
move(train_txt_paths, train_folder)
move(valid_img_paths, valid_folder)
move(valid_txt_paths, valid_folder)
"""