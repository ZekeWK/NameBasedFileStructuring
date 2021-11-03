#NameBasedFileStructuring by ZekeWK, use as you wish!

import os
import shutil
import re
from datetime import datetime

import config

def move():
    print("Move started")
    log = open('log.txt', 'a')

    errors = False

    files_to_sort = os.listdir(config.folder_to_structure)

    log.write(str(datetime.now()) + "| Activated in folder: " + config.folder_to_structure + "with the files: " + str(files_to_sort) + "\n")

    for file in files_to_sort:
        cur_path = config.folder_to_structure + "\\" + file
    
        new_dir = None
        for pattern, path in config.patterns:
            if re.search(pattern, file) != None:
                new_dir = (path)
                break
        
        if new_dir == None:
            log.write(str(datetime.now()) + "| Error for file: " + file + " . Could not find any pattern that matched the file \n")
            errors = True
            continue
        
        new_path = new_dir + "\\" + file

        if not os.path.exists(new_dir):
            log.write(str(datetime.now()) + "| Error for file: " + file + " . It's new directory: " + new_dir + " does not exist. \n")
            errors = True
            continue

        if file in os.listdir(new_dir):
            log.write(str(datetime.now()) + "| Error for file: " + file + " . File name already exists in new directory. \n")
            errors = True
            continue

        shutil.move(cur_path, new_path, copy_function = shutil.copy2)
        log.write(str(datetime.now()) + "| Moved file: " + file + " from:" + cur_path + " to: " + new_path + "\n")
    
    if errors:
        print("Atleast one error occurred during this session, further details can be found in the log.")
    
    log.write(str(datetime.now()) + "| Done in folder: " + config.folder_to_structure + "with the files: " + str(files_to_sort) + "\n")
    print("Done")
        
if __name__ == "__main__":
    move()