class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'


def print_blue(msg):
    print(f'\n{Colors.OKBLUE}{msg}{Colors.ENDC}')


def print_green(msg):
    print(f'\n{Colors.OKGREEN}{msg}{Colors.ENDC}')


def print_cyan(msg):
    print(f'\n{Colors.OKCYAN}{msg}{Colors.ENDC}')