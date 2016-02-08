from parse_config_file import parse_colors

colored_output = parse_colors()

def print_info(string):
    colored_output.print_info(string)

def print_error(string):
    colored_output.print_error(string)

def print_instruction(string):
    colored_output.print_instruction(string)

def print_side(string):
    colored_output.print_side(string)

def colored_prompt(prompt):
    return colored_output.colored_prompt(prompt)

def colored_getpass(prompt):
    colored_output.colored_getpass(prompt)
