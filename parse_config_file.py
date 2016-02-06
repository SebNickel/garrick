import configparser
import os
from load_config_file import locate_config_file
from colored_output import print_info, print_instruction, print_error

def get_config():
    
    garrick_dir, config_file_name = locate_config_file()

    config_file = os.path.join(garrick_dir, config_file_name)

    config = configparser.ConfigParser(allow_no_value = True)

    try:
        config.read(config_file)
    except Exception as exception:
        print_error('Something is wrong with your config file.')
        print_error('ConfigParser has thrown the following exception:')
        print()
        print(exception)
        print()
        write_example_config()

    return config

def write_example_config():

    garrick_dir, config_file_name = locate_config_file()

    print_info('Your config file is {}.'.format(os.path.join(garrick_dir, config_file_name)))
    print_info(
        'I am writing a file called {}.example into the same directory.'.format(config_file_name)
    )
    print_instruction(
        'You can work from this file to restore your garrick.conf file to a valid state.'
    )
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
        print_error('Error: There is no [database_files] section in your config file.')
        write_example_config()

    db_files = []

    for db_file in config['database_files']:
        db_files.append(db_file)
        
    if len(db_files) == 0:
        print_error('Error: No databases are listed in your config file.')
        print_instruction('Write a name for a database file into its [database_file] section.')
        print_info('This file will be created the next time you run garrick,')
        print_info('or it will be used if it already exists.')
        write_example_config()

    return db_files

def parse_editor():

    config = get_config()

    if not 'config' in config.sections():
        print_error('Error: There is no [config] section in your config file.')
        write_example_config()
        
    if not 'editor' in config['config']:
        print_error(
            'Error: There is no "editor" variable in the [config] section of your config file.'
        )
        write_example_config()

    editor = config['config']['editor']

    if editor == '' or editor == None:

        editor = os.getenv('EDITOR')
            
        if editor == None:
            print_error('Error: No editor is defined in your config file.')
            print_instruction(
                'Add the name of your favourite editor at the end of the line "editor = "'
            )
            print_instruction('so you can use it to edit your cards.')
            print_info("(This is normal if you haven't set the editor variable before.)")
            write_example_config()
    
    return editor
