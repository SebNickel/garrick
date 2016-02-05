import os

dir_name = '.garrick'
config_file_name = 'garrick.conf'

def locate_config_file():

    home_dir = os.getenv('HOME')

    if home_dir == None:
        print()
        print("Sorry, your system doesn't have a HOME environment variable set to any directory.")
        print("I am not equipped to deal with this situation :(")
        print("Which OS are you running?")
        print()
        raise Exception('HOME variable not set.')

    garrick_dir = os.path.join(home_dir, dir_name)

    if not os.path.exists(os.path.join(garrick_dir, config_file_name)):
        create_config_file(garrick_dir)
        
    return garrick_dir, config_file_name

def create_config_file(garrick_dir):

    if os.path.exists(garrick_dir):
        print()
        print('Uh oh.')
        print('There is a folder named ".garrick" in your home directory,')
        print('but it doesn\'t contain the file "garrick.conf".')
        print("If you've renamed or moved it, can you please change it back?")
        print('I am scared of breaking things. I will go now. Bai.')
        print()
        raise Exception('Directory exists.')

    os.mkdir(garrick_dir)
    
    default_editor = os.getenv('EDITOR')

    config_file_full_path = os.path.join(garrick_dir, config_file_name)

    with open(config_file_full_path, 'w') as f:
        f.write('[database_files]\n')
        f.write('cards.db\n\n')
        f.write('[config]\n')
        if default_editor == None:
            f.write('editor =')
        else:
            f.write('editor = {}'.format(default_editor))

    print('Created directory {}.'.format(garrick_dir))
    if default_editor == None:
        print('You might want to set the "editor" variable in {},'.format(config_file_full_path))
        print('so that you can edit your cards with your favourite editor.')
    else:
        print('Editor set to {}.'.format(default_editor))
        print('(You can change this in {}.)'.format(config_file_full_path))
