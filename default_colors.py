from colored_output import ColoredOutput

default_colors = ColoredOutput(
    'brightgreen',
    'brightred',
    'brightmagenta',
    'brightyellow',
    'brightcyan',
    'brightyellow'
)

def default_print_info(string):
    default_colors.print_info(string)

def default_print_error(string):
    default_colors.print_error(string)

def default_print_instruction(string):
    default_colors.print_instruction(string)

def default_print_side(string):
    default_colors.print_side(string)

def default_colored_prompt(prompt):
    return default_colors.colored_prompt(prompt)

def default_colored_getpass(prompt):
    default_colors.colored_getpass(prompt)
