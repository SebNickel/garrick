#!/usr/bin/env python
import os
import subprocess
from card import Card
from get_timestamp import get_timestamp
from getpass import getpass

editor = 'vim'
tmp_file = '.garricktmpfile'

def edit(card):

    with open(tmp_file, 'w') as tmp:
        tmp.write('EDIT THE CONTENTS OF THE CARD, SAVE IT AND QUIT THE EDITOR.\n')
        tmp.write('[FRONT]\n')
        tmp.write(card.front + '\n')
        tmp.write('[BACK]\n')
        tmp.write(card.back + '\n')
        tmp.write('[SCORE]\n')
        tmp.write(str(card.score))

    subprocess.run([editor,tmp_file])

    with open(tmp_file, 'r') as tmp:
        lines = tmp.readlines()
        
    os.remove(tmp_file)
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n').strip('\r')

    if not ('[FRONT]' in lines and '[BACK]' in lines and '[SCORE]' in lines):
        print('Error: The lines "[FRONT]", "[BACK]", and/or "[SCORE]" are messed up.')
        getpass('Hit Enter to start over.')
        return fix_your_edits(card)

    front_index = lines.index('[FRONT]')
    back_index = lines.index('[BACK]')
    score_index = lines.index('[SCORE]')

    front_lines = lines[front_index + 1:back_index]
    back_lines = lines[back_index + 1:score_index]

    front = '\n'.join(front_lines)
    back = '\n'.join(back_lines)
    
    last_viewed = get_timestamp()

    if len(lines) < score_index + 2:
        print('Error: No more score.')
        getpass('Hit Enter to go fix it.')
        faulty_card = Card(front, back, 0, last_viewed)
        return fix_your_edits(faulty_card)

    score_string = lines[score_index + 1]

    if not score_string.isdigit():
        print('Error: The score is no longer an integer.')
        getpass('Hit Enter to go fix it.')
        faulty_card = Card(front, back, 0, last_viewed)
        return fix_your_edits(faulty_card)

    score = int(score_string)

    if not int(score) in range(6):
        print('Error: {} is not a valid score.'.format(score))
        print('Valid scores are 0, 1, 2, 3, 4, 5.')
        getpass('Hit Enter to go fix it.')
        faulty_card = Card(front, back, score, last_viewed)
        return fix_your_edits(card)

    edited_card = Card(front, back, score, last_viewed)

    return edited_card

def fix_your_edits(card):

    return edit(card)

if __name__ == '__main__':

    card = Card('Hello World', 'This is a test.\nHere\'s another line.', 5, '2016-02-02 12:00')
    
    edited_card = edit(card)

    print('Front:')
    print()
    print(edited_card.front)
    print()
    print('Back:')
    print()
    print(edited_card.back)
    print()
    print('Score:')
    print()
    print(edited_card.score)
    print()
    print('Last viewed:')
    print()
    print(edited_card.last_viewed)
