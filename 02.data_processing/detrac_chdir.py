import shutil
import os
 
file_source = 'detrac_label'
file_destination = 'label'
 
get_folders = os.listdir(file_source)

for folder in get_folders:
    get_files = os.listdir(file_source + '/' + folder)
    for g in get_files:
        dir_0 = os.path.join(file_source, folder, g)
        dir_1 = os.path.join(file_source, folder)
        dir_2 = os.path.join(dir_1, folder[4:] + '_' + g)
        dir_3 = os.path.join(file_destination, g)
        shutil.move(dir_0, dir_3)
        

#for g in get_files:
#    shutil.move(file_source + g, file_destination)