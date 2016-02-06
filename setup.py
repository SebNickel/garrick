from setuptools import setup

setup(
    name = 'garrick',
    version = '1.0.dev3',
    py_modules = [
        'browse',
        'card', 
        'card_repository', 
        'db_connection', 
        'edit',
        'garrick',
        'get_timestamp', 
        'load_config_file',
        'new_card', 
        'new_cards', 
        'parse_config_file',
        'pick_card', 
        'pick_db_file', 
        'review_card', 
        'review_cards', 
        'unescape'
    ],
    data_files = [('', ['LICENSE.txt', 'README.md', 'garrick.conf.example'])],
    entry_points = {
        'console_scripts': [ 'garrick = garrick:main' ]
    },
    author = 'Sebastian Nickel',
    author_email = 'sebastianchristophnickel@gmail.com',
    description = 'Command-line flashcard app. Named after Jay Garrick, aka The Flash, first of his monicker.',
    license = 'MIT',
    keywords = 'flashcards flashcard command-line CLI',
    url = 'https://www.github.com/SebNickel/garrick'
)
