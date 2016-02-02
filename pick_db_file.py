import os

dir_name = '.garrick'
file_name = 'garrick.databases'

def locate_garrick_dir():

    home_dir = os.getenv('HOME')

    if home_dir == None:
        print()
        print("Sorry, your system doesn't have a HOME environment variable set to any directory.")
        print("I am not equipped to deal with this situation :(")
        print("Which OS are you running?")
        print()
        raise Exception('HOME variable not set.')

    garrick_dir = '{}/{}'.format(home_dir, dir_name)

    if not os.path.exists('{}/{}'.format(garrick_dir, file_name)):
        create_files_list(garrick_dir)
        
    return garrick_dir

def create_files_list(garrick_dir):

    if os.path.exists(garrick_dir):
        print()
        print('Uh oh.')
        print('There is a folder named ".garrick" in your home directory,')
        print('but it doesn\'t contain the file "garrick.databases".')
        print("If you've renamed or moved it, can you please change it back?")
        print('I am scared of breaking things. I will go now. Bai.')
        print()
        raise Exception('Directory exists.')

    os.mkdir(garrick_dir)

    with open('{}/{}'.format(garrick_dir, file_name), 'w') as f:
        f.write('garrick.db')

def read_files_list(files_list_location):

    db_files = []

    with open(files_list_location, 'r') as f:
        for line in f:
            db_file = line.strip('\r').strip('\n')
            db_files.append(db_file)

    return db_files

def pick_db_file():

    garrick_dir = locate_garrick_dir()
    
    files_list_location = '{}/{}'.format(garrick_dir, file_name)

    db_files = read_files_list(files_list_location)

    if len(db_files) == 0:

        print()
        print('Error: The databases file, {}, is empty.'.format(files_list_location))
        print('Write a name for a new database file into it, and it will be created the next time')
        print('you run garrick. (Or it will be used if it already exists.)')
        print()

        raise Exception('No database configured.')

    elif len(db_files) > 1:

        for i in range(len(db_files)):
            print('{}. {}'.format(i + 1, db_files[i]))

        while True:
            selection = input('Enter the number of the database to use: ')
            if selection.isdigit() and int(selection) in range(1, len(db_files)):
                db_number = int(selection)
                break

        db_file = db_files[db_number - 1]

    else:

        db_file = db_files[0]

    db_full_path = '{}/{}'.format(garrick_dir, db_file)

    return db_full_path
