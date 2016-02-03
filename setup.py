from setuptools import setup, find_packages

setup(
    name = 'garrick',
    version = '1.0.dev1',
    py_modules = [
        'card', 
        'card_repository', 
        'db_connection', 
        'get_timestamp', 
        'new_card', 
        'new_cards', 
        'pick_card', 
        'pick_db_file', 
        'review_card', 
        'review_cards', 
        'garrick', 
        'edit',
        'unescape'
    ],
    include_package_data = True,
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
