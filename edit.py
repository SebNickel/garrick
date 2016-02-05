import os
import subprocess
from getpass import getpass
from card import Card
from get_timestamp import get_timestamp
from parse_config_file import parse_editor

tmp_file = '.garricktmpfile'

def fix_your_edits(card):

    return edit(card)

def edit(card):

    editor = parse_editor()

    with open(tmp_file, 'w') as tmp:
        tmp.write('EDIT THE CONTENTS OF THE CARD, SAVE IT AND QUIT THE EDITOR.\n')
        tmp.write('[FRONT]\n')
        tmp.write(card.front + '\n')
        tmp.write('[BACK]\n')
        tmp.write(card.back + '\n')
        tmp.write('[SCORE]\n')
        tmp.write(str(card.score))

    subprocess.run([editor, tmp_file])

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

    if (not score_string.isdigit()) or (not int(score_string) in range(6)):
        print('Error: {} is not a valid score.'.format(score))
        print('Valid scores are 0, 1, 2, 3, 4, 5.')
        getpass('Hit Enter to go fix it.')
        faulty_card = Card(front, back, 0, last_viewed)
        return fix_your_edits(card)
    
    score = int(score_string)

    edited_card = Card(front, back, score, last_viewed)

    return edited_card
