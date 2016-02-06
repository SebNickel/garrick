import os
from parse_config_file import parse_db_files
from load_config_file import locate_config_file
from colored_output import colored_prompt

def pick_db_file():

    db_files = parse_db_files()
    
    garrick_dir, _ = locate_config_file()

    if len(db_files) == 1:

        db_file = db_files[0]

    else:

        for i in range(len(db_files)):
            print('{}. {}'.format(i + 1, db_files[i]))

        while True:
            selection = colored_prompt('Enter the number of the database file to use: ')
            if selection.isdigit() and int(selection) in range(1, len(db_files) + 1):
                db_number = int(selection)
                break

        db_file = db_files[db_number - 1]

    return os.path.join(garrick_dir, db_file)
