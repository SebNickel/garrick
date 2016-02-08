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
    colored_output.print_info(string)

def default_print_error(string):
    colored_output.print_error(string)

def default_print_instruction(string):
    colored_output.print_instruction(string)

def default_print_side(string):
    colored_output.print_side(string)

def default_colored_prompt(prompt):
    return colored_output.colored_prompt(prompt)

def default_colored_getpass(prompt):
    colored_output.colored_getpass(prompt)
