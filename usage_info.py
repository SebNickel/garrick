def print_usage_info(args):

    if args[1] not in ['-h', '--help']:
        print('{}: invalid command(s): {}'\
            .format(args[0], ' '.join(args[1:]))
        )
        print()

    print('Usage: garrick [COMMAND]')
    print()
    print('Launching garrick without arguments starts a regular review session, provided that')
    print('your card database isn\'t empty.')
    print()
    print('If more than one database is referenced in the [databases] section of your config')
    print('file, garrick will ask you which database to use before starting.')
    print()
    print('Commands:')
    print('\t-n\tCreate cards starting in one-way mode.')
    print('\t-n2\tCreate cards starting in two-way mode.')
    print('\t-s\tCreate cards starting in single-line and one-way mode.')
    print('\t-s2\tCreate cards starting in single-line and two-way mode.')
    print('\t-e\tCreate cards starting in editor-mode and in one-way mode.')
    print('\t-e2\tCreate cards starting in editor-mode and in two-way mode.')
    print('\t-b\tBrowse cards by matching either side of cards to a regular expression.')
    print('\t-bf\tBrowse cards by matching the front of cards to a regular expression.')
    print('\t-bb\tBrowse cards by matching the back of cards to a regular expression.')
    print('\t-bs\tBrowse cards with a certain score.')
    print('\t-bl\tBrowse cards in the order of their "last viewed" timestamp.')
    print('\t-br\tBrowse cards in the reverse order of their "last viewed" timestamp.')
