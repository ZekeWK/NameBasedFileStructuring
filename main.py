#NameBasedFileStructuring by ZekeWK, use as you wish!

from os import path, listdir, remove, chdir
from os.path import isdir, exists
import shutil
from re import search
from sys import stdout
import logging


# TODO write comment Modifies list...
def structure_dir(unstructured_dir, dir_patterns):
    chdir(unstructured_dir)
    unstructured_files = listdir()

    logging.info(f"Activated in directory {unstructured_dir} containing the files {', '.join(unstructured_files)}.")

    for file in unstructured_files:
        new_dirs = []
        error = False
        for (pattern, new_dir) in dir_patterns:
            if search(pattern, file) is None:
                continue

            new_dirs.append(new_dir)

            if not isdir(new_dir):
                logging.warning(f"File {file} not moved as directory {new_dir} does not exist.")
                error = True
                continue

            new_path = path.join(new_dir, file)

            if exists(new_path):
                logging.warning(f"File {file} not moved as directory {new_dir} already contains file with same name.")
                error = True


        if not new_dirs:
            logging.warning(f"File {file} not moved as it did not match any pattern.")
            continue

        if error:
            continue

        for new_dir in new_dirs:
            shutil.copy(file, new_dir)
            logging.info(f"File {file} copied to {new_dir}.")

        remove(file)
        logging.info(f"File removed from {unstructured_dir}.")

    
    logging.info(f"Done in directory {unstructured_dir} containing files {', '.join(listdir())}.")

if __name__ == "__main__":
    print("Started")

    fh = logging.FileHandler("log.txt")
    fh.setLevel(logging.INFO)

    sh = logging.StreamHandler(stdout)
    sh.setLevel(logging.WARNING)

    logging.basicConfig(format="%(asctime)s | %(levelname)s | %(message)s", handlers=[sh, fh], level=logging.INFO)

    import config

    structure_dir(config.unstructured_dir, config.dir_patterns)
    print("Done")
