import glob, os
import argparse
import random
from collections import Counter
parser = argparse.ArgumentParser()
parser.add_argument('train_pct',help="percentage of images to be used for training, the rest are used for validation and testing",
                    type=int)
parser.add_argument('valid_pct',help="percentage of images to be used for validation, the rest are used for training and testing",
                    type=int)
parser.add_argument('test_pct',help="percentage of images to be used for validation, the rest are used for training and testing",
                    type=int)
parser.add_argument('dir_name',help="path to directory with images and yolo annotations",
                    type=str)
args = parser.parse_args()

if (args.train_pct + args.valid_pct + args.test_pct) != 100:
    print('The accumulation of percentages must be 100')
    print('Job terminated')
    exit(0)

def file_path_gen(path):
    file_path_list = []
    for (root, _, files) in os.walk(path):
        for file in files:
            if file[-4:] == '.jpg':
                file_path = os.path.join(root, file)
                file_path_list.append(file_path)

    return file_path_list

file_paths = file_path_gen(args.dir_name)





print('finish')