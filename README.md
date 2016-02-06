# garrick
Command-line flashcard app written in Python 3.

Named after Jay Garrick, aka The Flash, first of his monicker.

### Installing
If you have git, python3, and setuptools:
```
$ git clone https://github.com/SebNickel/garrick.git
$ cd garrick
# python setup.py install
```

### Todo
* ~~Write install script~~
* Improve the card selection algorithm (current algorithm is a proof of concept, though it works fine).
* ~~Allow easy editing and deleting of cards.~~
* ~~Add a "single line mode", for entering cards with only one line on each side without the need to press Ctrl+D.~~
* ~~Allow using other editors, not just vim.~~
* Allow creating new cards in "editor mode".
* ~~Allow browsing cards.~~
* Allow editing and deleting "sister cards" together (i.e. both versions of a two-way card).
* Allow splitting one card into several cards when editing.
* ~~Add coloured output, probably using the colorama library for better portability.~~
* ~~Catch configparser exceptions.~~
* ~~Merge review\_cards in with the browse module, using iterators.~~
* Make colours user-definable.
