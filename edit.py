import os
import subprocess
from card import Card
from timestamps import get_timestamp
from parse_config_file import parse_editor
from user_colors import print_info, print_error, colored_getpass

tmp_file = '.garricktmpfile'

editor = parse_editor()

def write_edits(card, tags):
    
    with open(tmp_file, 'w') as tmp:
        tmp.write('EDIT THE CONTENTS OF THE CARD, SAVE IT AND QUIT THE EDITOR.\n')
        tmp.write(tags[0] + '\n')
        tmp.write(card.front + '\n')
        tmp.write(tags[1] + '\n')
        tmp.write(card.back + '\n')
        tmp.write(tags[2] + '\n')
        tmp.write(str(card.score))

    subprocess.run([editor, tmp_file])

    with open(tmp_file, 'r') as tmp:
        lines = tmp.readlines()
        
    os.remove(tmp_file)

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n').strip('\r')

    return lines

def parse_edits(lines, tags):

    if not all([x in lines for x in tags]):
        print_error('Error: The lines "{}", "{}", and/or "{}" are messed up.'.format(*tags))
        colored_getpass('Hit Enter to start over.')
        return None, None

    front_index = lines.index(tags[0])
    back_index = lines.index(tags[1])
    score_index = lines.index(tags[2])

    front_lines = lines[front_index + 1:back_index]
    back_lines = lines[back_index + 1:score_index]

    front = '\n'.join(front_lines)
    back = '\n'.join(back_lines)
    
    last_viewed = get_timestamp()

    if len(lines) < score_index + 2:
        print_error('Error: No score.')
        colored_getpass('Hit Enter to go fix it.')
        faulty_card = Card(front, back, 0, last_viewed)
        faulty = True
        return faulty_card, faulty

    score_string = lines[score_index + 1]

    if (not score_string.isdigit()) or (not int(score_string) in range(6)):
        print_error('Error: {} is not a valid score.'.format(score_string))
        print_info('Valid scores are 0, 1, 2, 3, 4, 5.')
        colored_getpass('Hit Enter to go fix it.')
        faulty_card = Card(front, back, 0, last_viewed)
        faulty = True
        return faulty_card, faulty
    
    score = int(score_string)

    edited_card = Card(front, back, score, last_viewed)

    faulty = False

    return edited_card, faulty

def edit(card, two_way_card):
    
    if two_way_card:
        tags = ['[SIDE 1]', '[SIDE 2]', '[SCORE]']
    else:
        tags = ['[FRONT]', '[BACK]', '[SCORE]']

    lines = write_edits(card, tags)
    
    edited_card, faulty = parse_edits(lines, tags)

    if edited_card == None:
        return edit(card, two_way_card)

    if faulty:
        return edit(edited_card, two_way_card)

    return edited_card
