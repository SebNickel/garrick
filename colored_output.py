from colorama import Fore, Style
from getpass import getpass

def color_map(color_name):
    return {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.BLACK,
        'brightblack': Fore.BLACK + Style.BRIGHT,
        'brightred': Fore.RED + Style.BRIGHT,
        'brightgreen': Fore.GREEN + Style.BRIGHT,
        'brightyellow': Fore.YELLOW + Style.BRIGHT,
        'brightblue': Fore.BLUE + Style.BRIGHT,
        'brightmagenta': Fore.MAGENTA + Style.BRIGHT,
        'brightcyan': Fore.CYAN + Style.BRIGHT,
        'brightwhite': Fore.BLACK + Style.BRIGHT
    }.get(color_name, Fore.WHITE)

class ColoredOutput:

    def __init__(self, info, error, instruction, side, prompt, silent_prompt):
        self.info_color = color_map(info)
        self.error_color = color_map(error)
        self.instruction_color = color_map(instruction)
        self.side_color = color_map(side)
        self.prompt_color = color_map(prompt)
        self.silent_prompt_color = color_map(silent_prompt)
        
    def print_info(self, string):
        print(self.info_color + string + Style.RESET_ALL)
    
    def print_error(self, string):
        print(self.error_color + string + Style.RESET_ALL)
    
    def print_instruction(self, string):
        print(self.instruction_color + string + Style.RESET_ALL)
    
    def print_side(self, string):
        print(self.side_color + string + Style.RESET_ALL)
    
    def colored_prompt(self, prompt):
        user_input = input(self.prompt_color + prompt + Style.RESET_ALL)
        return user_input
    
    def colored_getpass(self, prompt):
        getpass(self.silent_prompt_color + prompt + Style.RESET_ALL)
