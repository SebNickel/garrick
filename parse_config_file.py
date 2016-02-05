import configparser
import os
from load_config_file import locate_config_file

def get_config():
    
    garrick_dir, config_file_name = locate_config_file()

    config_file = os.path.join(garrick_dir, config_file_name)

    config = configparser.ConfigParser(allow_no_value = True)
    config.read(config_file)

    return config

def write_example_config():

    garrick_dir, config_file_name = locate_config_file()

    print('Your config file is {}.'.format(os.path.join(garrick_dir, config_file_name)))
    print('I am writing a file called {}.example into the same directory.'.format(config_file_name))
    print('You can work from this file to restore your garrick.conf file to a valid state.')
    print()

    with open(os.path.join(garrick_dir, '{}.example'.format(config_file_name)), 'w') as f:
        f.write('[database_files]\n')
        f.write('linux.db\n')
        f.write('spanish.db\n')
        f.write('economics.db\n')
        f.write('pokemon.db\n\n')
        f.write('[config]\n')
        f.write('editor = vim')

    raise Exception('Invalid or incomplete config file.')

def parse_db_files():

    config = get_config()

    if not 'database_files' in config.sections():
        print('Error: There is no [database_files] section in your config file.')
        write_example_config()

    db_files = []

    for db_file in config['database_files']:
        db_files.append(db_file)
        
    if len(db_files) == 0:
        print('Error: No databases are listed in your config file.')
        print('Write a name for a database file into its [database_file] section.')
        print('or it will be used if it already exists.')
        print('This file will be created the next time you run garrick,')
        write_example_config()

    return db_files

def parse_editor():

    config = get_config()

    if not 'config' in config.sections():
        print('Error: There is no [config] section in your config file.')
        write_example_config()
        
    if not 'editor' in config['config']:
        print('Error: There is no "editor" variable in the [config] section of your config file.')
        write_example_config()

    editor = config['config']['editor']

    if editor == '' or editor == None:

        editor = os.getenv('EDITOR')
            
        if editor == None:
            print('Error: No editor is defined in your config file.')
            print('Add the name of your favourite editor at the end of the line "editor = "')
            print('so you can use it to edit your cards.')
            print("(This is normal if you haven't set the editor variable before.)")
            write_example_config()
    
    return editor
