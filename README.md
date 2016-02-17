# garrick
Command-line flashcard app written in Python 3.

Named after Jay Garrick, aka The Flash, first of his monicker.

### Contents
- [Installing](#installing)
- [User guide](#userguide)
- [Current (known) problems](#problems)
  - [Card selection algorithm](#algorithm)
  - [Inaccurate countdown during regular review](#countdown)
- [Todo](#todo)

### <a name="installing"></a> Installing
If you have git, python3, and setuptools:
```
$ git clone https://github.com/SebNickel/garrick.git
$ cd garrick
# python setup.py install
```

### <a name="userguide"></a> User guide

Have a look at the [current (known) problems](#problems) (particularly to do with the card selection algorithm), lest you expect too much from the current version. Please do improve garrick if you're the garrick-improving type.

### <a name="problems"></a> Current (known) problems

I do not promise to fix these soon. If you are interested in doing so, please fork and hack.

##### <a name="algorithm"></a> Card selection algorithm

The current card selection algorithm remains little more than a proof of concept. It is noticeably flawed.
The most obvious goal for future releases is to replace it with one or more good algorithm(s). 
E.g. the SM-17 algorithm is a popular choice, and is described [here](http://www.supermemopedia.com/wiki/Algorithm_SM-17).

(Note that the app provides several ways of browsing through cards that do not rely on the flawed algorithm.)

In the current implementation:
- Each card has a score and a "last_viewed" entry.
- After viewing a card, the user is asked to score herself from 0 to 5.
- The card's score is then updated accordingly, and its last\_viewed value is updated to the current timestamp.
- If the card is a two-way card, the last\_viewed value of the "flipped version" of the card is also bumped, but not to the current time. Instead, garrick takes the interval between the flipped version's last\_viewed value and the current time, divides it by two, and adds that to the flipped version's last_viewed timestamp.
- When selecting a card to display, garrick first chooses one of the available scores at random. The probabilities are: P(0) = 0.4, P(1) = 0.3, P(2) = 0.15, P(3) = 0.1, P(4) = 0.035, P(5) = 0.015.
- Garrick then selects the card with the oldest last\_viewed value among all cards with this score. If no card with this score exists, garrick goes back to the previous step to pick another score.

The glaring problem here is that, so long as only a small portion of your cards have a high score, these cards will show up too often. While garrick infrequently fetches any highly scored card, the lacking variety among them quickly becomes apparent on those occasions when garrick does choose to do so.

##### <a name="countdown"></a> Inaccurate countdown during regular review

When browsing through cards in any of the various ways, garrick outputs the number of cards it has found that match your browsing criterion, and displays the first one. As you then go through the cards, garrick shows you how many matching cards are left after each step.

During a regular review, garrick first outputs the total number of cards in the database, and then counts down from there with any card you view. However the countdown in this case is rather meaningless. As cards with different scores come up at different frequencies, it quickly becomes inaccurate as a count of the cards in the database that you have not yet viewed during the current review session. The session also doesn't end when the count hits zero. Garrick then simply stops displaying a count.

This need not ruin your garrick experience in any way, and it remains useful as a way of seeing how many cards you've viewed. But be aware that this particular cake is a lie.

### <a name="todo"></a> Todo
* ~~Write install script~~
* Improve the card selection algorithm (current algorithm is a proof of concept, though it works fine ~~for one-way cards~~).
* ~~Allow easy editing and deleting of cards.~~
* ~~Add a "single line mode", for entering cards with only one line on each side without the need to press Ctrl+D.~~
* ~~Allow using other editors, not just vim.~~
* ~~Allow creating new cards in "editor mode".~~
* ~~Allow browsing cards.~~
* ~~Allow editing and deleting "sister cards" together (i.e. both versions of a two-way card).~~
* ~~Allow splitting one card into several cards when editing.~~
* ~~Add coloured output, probably using the colorama library for better portability.~~
* ~~Catch configparser exceptions.~~
* ~~Merge review\_cards in with the browse module, using iterators.~~
* ~~Make colours user-definable.~~
* ~~Fix encoding issues.~~
* ~~Usage info.~~
* User guide.
* ~~Major cleanup.~~
* 1.0 release ^^
