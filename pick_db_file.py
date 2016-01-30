files_list_location = 'garrick.databases'

def read_files_list():

    db_files = []

    with open(files_list_location, 'r') as f:
        for line in f:
            db_file = line.strip('\r').strip('\n')
            db_files.append(db_file)

    return db_files

def pick_db_file():

    db_files = read_files_list()

    if len(db_files) == 0:

        print('Error: The databases file (ordinarily called "garrick.databases") is empty.')
        print('Write a name for a new database file into it, and it will be created the next time')
        print('you run garrick. (Or it will be used if it already exists.)')
        print()

        raise Exception('No database configured.')

    elif len(db_files) > 1:

        for i in range(len(db_files)):
            print('{}. {}'.format(i + 1, db_files[i]))

        db_number = input('Enter the number of the database to use: ')

        while not (db_number.isdigit and db_number in range(1, len(db_files))):
            db_number = input('Invalid selection. Try again: ')

        selected_db_file = db_files[db_number - 1]

        return selected_db_file

    else:

        return db_files[0]
