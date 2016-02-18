import configparser
import os
from load_config_file import locate_config_file
from default_colors import default_print_info, default_print_error, default_print_instruction
from colored_output import ColoredOutput
from pkg_resources import Requirement, resource_filename
from shutil import copyfile

def write_example_config():
    
    garrick_dir, config_file_name = locate_config_file()

    default_print_info(
        'Your config file is {}.'.format(os.path.join(garrick_dir, config_file_name))
    )
    default_print_info(
        'I am writing a file called {}.example into the same directory.'.format(config_file_name)
    )
    default_print_instruction(
        'You can work from this file to restore your garrick.conf file to a valid state.'
    )
    print()

    example_config_file = resource_filename(Requirement.parse('garrick'), 'garrick.conf.example')

    copyfile(example_config_file, os.path.join(garrick_dir, '{}.example'.format(config_file_name)))

    raise Exception('Invalid or incomplete config file.')

def get_config():
    
    garrick_dir, config_file_name = locate_config_file()

    config_file = os.path.join(garrick_dir, config_file_name)

    config = configparser.ConfigParser(allow_no_value = True)

    try:
        config.read(config_file)
    except Exception as exception:
        print()
        default_print_error('Something is wrong with your config file.')
        default_print_error('ConfigParser has thrown the following exception:')
        print()
        print(exception)
        print()
        write_example_config()

    return config

def parse_db_files():

    config = get_config()

    if not 'database_files' in config.sections():
        print()
        default_print_error(
            'Error: There is no [database_files] section in your config file.'
        )
        print()
        write_example_config()

    db_files = []

    for db_file in config['database_files']:
        db_files.append(db_file)
        
    if len(db_files) == 0:
        print()
        default_print_error(
            'Error: No databases are listed in your config file.'
        )
        default_print_instruction(
            'Write a name for a database file into its [database_files] section.'
        )
        default_print_info('This file will be created the next time you run garrick,')
        default_print_info('or it will be used if it already exists.')
        print()
        write_example_config()

    return db_files

def parse_editor():

    config = get_config()

    if not 'config' in config.sections():
        print()
        default_print_error('Error: There is no [config] section in your config file.')
        print()
        write_example_config()
        
    if not 'editor' in config['config']:
        print()
        default_print_error(
            'Error: There is no "editor" variable in the [config] section of your config file.'
        )
        print()
        write_example_config()

    editor = config['config']['editor']

    if editor == '' or editor == None:

        editor = os.getenv('EDITOR')
            
        if editor == None:
            print()
            default_print_error('Error: No editor is defined in your config file.')
            default_print_instruction(
                'Add the name of your favourite editor at the end of the line "editor = "'
            )
            default_print_instruction('so you can use it to edit your cards.')
            default_print_info(
                "(This is normal if you haven't set the editor variable before.)"
            )
            print()
            write_example_config()
    
    return editor

def parse_colors():

    config = get_config()

    if not 'config' in config.sections():
        print()
        default_print_error('Error: There is no [config] section in your config file.')
        print()
        write_example_config()

    if 'info' in config['config']:
        info_color = config['config']['info']
    else:
        info_color = 'brightgreen'

    if 'error' in config['config']:
        error_color = config['config']['error']
    else:
        error_color = 'brightred'

    if 'instruction' in config['config']:
        instruction_color = config['config']['instruction']
    else:
        instruction_color = 'brightmagenta'

    if 'side_of_card' in config['config']:
        side_color = config['config']['side_of_card']
    else:
        side_color = 'brightyellow'

    if 'prompt' in config['config']:
        prompt_color = config['config']['prompt']
    else:
        prompt_color = 'brightcyan'

    if 'silent_prompt' in config['config']:
        silent_prompt_color = config['config']['silent_prompt']
    else:
        silent_prompt_color = 'brightyellow'

    return ColoredOutput(
        info_color, 
        error_color,
        instruction_color,
        side_color,
        prompt_color,
        silent_prompt_color
    )
