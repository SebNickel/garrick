import os
from default_colors import default_print_info, default_print_error, default_print_instruction

dir_name = '.garrick'
config_file_name = 'garrick.conf'

def locate_config_file():

    home_dir = os.getenv('HOME')

    if home_dir == None:
        print()
        default_print_error(
            "Sorry, your system doesn't have a HOME environment variable set to any directory."
        )
        default_print_error("I am not equipped to deal with this situation :(")
        default_print_error("Which OS are you running?")
        print()
        raise Exception('HOME variable not set.')

    garrick_dir = os.path.join(home_dir, dir_name)

    if not os.path.exists(os.path.join(garrick_dir, config_file_name)):

        if os.path.exists(garrick_dir):

            print()
            default_print_error('Uh oh.')
            default_print_error(
                'There is a folder named "{}" in your home directory,'.format(dir_name)
            )
            default_print_error('but it doesn\'t contain the file "{}".'.format(config_file_name))
            default_print_error("If you've renamed or moved it, can you please change it back?")
            default_print_error('I am scared of breaking things. I will go now. Bai.')
            print()
            raise Exception('Directory exists.')

        create_config_file(garrick_dir)
        
    return garrick_dir, config_file_name

def create_config_file(garrick_dir):

    os.mkdir(garrick_dir)
    
    default_editor = os.getenv('EDITOR')

    config_file_full_path = os.path.join(garrick_dir, config_file_name)

    with open(config_file_full_path, 'w') as f:
        f.write('[database_files]\n')
        f.write('cards.db\n\n')
        f.write('[config]\n')
        if default_editor == None:
            f.write('editor =\n')
        else:
            f.write('editor = {}\n'.format(default_editor))
        f.write('\n# COLOURS\n')
        f.write('# Available choices are:\n')
        f.write('# black, red, green, yellow, blue, magenta, cyan, white,\n')
        f.write('# brightblack, brightred, etc.\n')
        f.write('info = brightgreen\n')
        f.write('error = brightred\n')
        f.write('instruction = brightmagenta\n')
        f.write('side_of_card = brightyellow\n')
        f.write('prompt = brightcyan\n')
        f.write('silent_prompt = brightyellow\n')

    print_info('Created directory {}.'.format(garrick_dir))
    if default_editor == None:
        default_print_instruction(
            'You might want to set the "editor" variable in {},'.format(config_file_full_path)
        )
        default_print_instruction('so that you can edit your cards with your favourite editor.')
    else:
        default_print_info('Editor set to {}.'.format(default_editor))
        default_print_instruction('(You can change this in {}.)'.format(config_file_full_path))
