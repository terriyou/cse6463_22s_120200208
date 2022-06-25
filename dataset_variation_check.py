import os

dir_name = 'obj'

variation = []
variation_cnt = []

def file_path_gen(path):
    for (root, _, files) in os.walk(path):
        idx_tmp = 0
        file_name_tmp = '20011'
        for idx, file in enumerate(files):
            if file_name_tmp != file[:5]:
                inpt_idx = idx - idx_tmp
                variation_cnt.append(str(inpt_idx))
                idx_tmp = idx
                file_name_tmp = file[:5]
            if file[:5] not in variation:
                variation.append(file[:5])

file_path_gen(dir_name)

f = open('each_vari_cnt_of_dataset_dirs.txt','w')
f.write(' '.join(variation))
f.write('\n')
for cnt in variation_cnt:
    f.write(cnt)
    if len(cnt) == 3:
        f.write('   ')
    elif len(cnt) == 4:
        f.write('  ')
    else:
        f.write('\n')
f.close()
