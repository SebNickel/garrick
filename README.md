# garrick
Command-line flashcard app written in Python 3.

Named after Jay Garrick, aka The Flash, first of his monicker.

### Contents
- [Installing](#installing)
- [User guide](#userguide)
  - [Usage info](#usage)
  - [Creating cards](#creating)
  - [Viewing/browsing cards](#viewing)
  - [Configuration](#config)
- [Current (known) problems](#problems)
  - [Card selection algorithm](#algorithm)
  - [Inaccurate countdown during regular review](#countdown)
- [Todo](#todo)

### <a name="installing"></a>Installing
If you have git, python3, and setuptools:
```
$ git clone https://github.com/SebNickel/garrick.git
$ cd garrick
# python setup.py install
```

### <a name="userguide"></a>User guide

Have a look at the [current (known) problems](#problems) (particularly to do with the card selection algorithm), lest you expect too much from the current version. Please do improve garrick if you're the garrick-improving type.

##### <a name="usage"></a>Usage info

```
Usage: garrick [COMMAND]

Launching garrick without arguments starts a regular review session, provided that
your card database isn't empty.

If more than one database is referenced in the [database_files] section of your config
file, garrick will ask you which database to use before starting.

Commands:
	-n    Create cards starting in one-way mode.
	-n2	  Create cards starting in two-way mode.
	-s	  Create cards starting in single-line and one-way mode.
	-s2	  Create cards starting in single-line and two-way mode.
	-e	  Create cards starting in editor mode and in one-way mode.
	-e2	  Create cards starting in editor mode and in two-way mode.
	-b	  Browse cards by matching either side of cards to a regular expression.
	-bf	  Browse cards by matching the front of cards to a regular expression.
	-bb	  Browse cards by matching the back of cards to a regular expression.
	-bs	  Browse cards with a certain score.
	-bl	  Browse cards in the order of their "last viewed" timestamp.
	-br	  Browse cards in the reverse order of their "last viewed" timestamp.
```

##### <a name="creating"></a>Creating cards

Cards can be created using various "modes", some of which can mix and match.
- **Normal multi-line mode** (default): Hitting Enter saves the current line to the current side of the card and opens a new line. Ctrl+D finishes the current side.
- **Single-line mode**: Hitting Enter finishes the current side of the card.
- **Editor mode**: Enter new cards using a text editor. Saving and quitting the editor saves the card. You're then presented with a menu. Simply hitting Enter reopens the editor so you can write the next card.
- **One-way mode** (default): Creates one-way cards. (See below.)
- **Two-way mode**: Creates two-way cards.

A one-way card has a front and a back. When reviewing cards, the user is always presented with its front and prompted to remember what's on the back of the card.

A two-way card has two sides and can be presented to the user by showing either side first. Internally, a two-way card is simply two different database entries with the front and the back inverted. Garrick sometimes refers to them as "flipped versions" of a two-way card.

You can choose the modes in which card creation begins by choosing the appropriate command-line option as listed above. You can also toggle the various modes in between the creation of any two cards. Outside of "editor mode", press Ctrl+C to get a menu. (This will discard the current card!)

##### <a name="viewing"></a>Viewing/browsing cards

Start a "regular review" (using the current flawed algorithm, as described [below](#algorithm)) by running "garrick" without arguments, and then selecting a database if you have more than one.

Alternatively, run garrick with one of the various options beginning with _b_ to browse your cards by one of the available criteria. Garrick will prompt you for a regular expression or a score if this is the criterion you've chosen.

After that, the interface is the same in any case: Garrick displays the front of a card, and waits until you hit Enter. It then displays the back of the card, and asks you to score yourself from 0 to 5. The higher the score, the less likely garrick should be to show you that card in the future. (But see [below](#algorithm).)

Alternatively, enter _o_ (for _options_) instead of a score. You can then enter _d_ to delete the card, or _e_ to edit it in a text editor. You will also get to edit your score inside the editor.

##### <a name="config"></a>Configuration

When you first run garrick, it creates a directory called _.garrick_ in your home directory, which initially contains just the configuration file _garrick.conf_.

Use this config file to
- add one or more new database(s). Any newly added database listed in the [database_files] section (one DB name per line) will be created the next time you run garrick. It is stored inside a file with the name you have given it in _garrick.conf_, which garrick writes into the _.garrick_ directory. By default, the config file lists one database named "cards.db".
- set your text editor. If your EDITOR environment variable is set at the time _garrick.conf_ is created, garrick automatically sets that as your editor in the config file. If you later try to edit a card or write a new card in editor mode, and no editor is set in _garrick.conf_, garrick will still look up your EDITOR environment variable and use that if it's set.
- set the colours for garrick's different types of output. The available choices are listed in a comment inside _garrick.conf_.

To rename a database:
- Rename the actual file (found in the _.garrick_ directory).
- Change the entry in _garrick.conf_'s [database_files] section to match the new filename.

If you mess up your config file and garrick finds it unusable, it copies _garrick.conf.example_ into the _.garrick_ directory to show you how it's done. If you want to get your copy of that file even though your _garrick.conf_ causes no error, one way of getting it is to deliberately break your config file, e.g. by deleting one of the section headers.

### <a name="problems"></a>Current (known) problems

I do not promise to fix these soon. If you are interested in doing so, please fork and hack.

##### <a name="algorithm"></a>Card selection algorithm

The current card selection algorithm remains little more than a proof of concept. It is noticeably flawed.
The most obvious goal for future releases is to replace it with one or more good algorithm(s). 
E.g. the SM-17 algorithm is a popular choice, and is described [here](http://www.supermemopedia.com/wiki/Algorithm_SM-17).

(Note that garrick provides several ways of browsing through cards that do not rely on the flawed algorithm.)

In the current implementation:
- Each card has a score and a _last\_viewed_ entry.
- After viewing a card, the user is asked to score herself from 0 to 5.
- The card's score is then updated accordingly, and its _last\_viewed_ value is updated to the current timestamp.
- If the card is a two-way card, the _last\_viewed_ value of the "flipped version" of the card is also bumped, but not to the current time. Instead, garrick takes the interval between the flipped version's _last\_viewed_ value and the current time, divides it by two, and adds that to the flipped version's _last_viewed_ timestamp.
- When selecting a card to display, garrick first chooses one of the available scores at random. The probabilities are: P(0) = 0.4, P(1) = 0.3, P(2) = 0.15, P(3) = 0.1, P(4) = 0.035, P(5) = 0.015.
- Garrick then selects the card with the oldest _last\_viewed_ value among all cards with this score. If no card with this score exists, garrick goes back to the previous step to pick a new score.

The glaring problem here is that, so long as only a small portion of your cards have a high score, these cards will show up too often. While garrick infrequently fetches any highly scored card, the lacking variety among them quickly becomes apparent on those occasions when garrick does choose to do so.

##### <a name="countdown"></a>Inaccurate countdown during regular review

When browsing through cards in any of the various ways, garrick outputs the number of cards it has found that match your browsing criterion, and displays the first one. As you then go through the cards, garrick shows you how many matching cards are left after each step.

During a regular review, garrick first outputs the total number of cards in the database, and then counts down from there with any card you view. However the countdown in this case is rather meaningless. As cards with different scores come up at different frequencies, it quickly becomes inaccurate as a count of the cards in the database that you have not yet viewed during the current review session. The session also doesn't end when the count hits zero. Garrick then simply stops displaying a count.

This need not ruin your garrick experience in any way, and it remains useful as a way of seeing how many cards you've viewed. But be aware that this particular cake is a lie.

### <a name="todo"></a>Todo
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
* ~~User guide.~~
* ~~Major cleanup.~~
* 1.0 release ^^
