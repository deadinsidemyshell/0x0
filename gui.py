from PyInquirer import style_from_dict, Token, Separator, prompt
from rich.console import Console


#MODELS :

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

INPUT_HOST = [
    {
        'type': 'input',
        'name': 'host',
        'message': 'Enter single/multiple target adress (IPV4/WWW) :',
        #'validate': Ip_Validator,
        'default': 'scanme.nmap.org',
    }
]



MODE = [
    {
        'type': 'checkbox',
        'message': '\n',
        'name': 'toppings',
        'choices': [
            Separator("== CHOOSE WEAPON =="),
            {
                'name' : 'IA',
            },
            {
                'name' : 'ROOTS',
            },
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

INPUT_ARGS = [
    {
        'type': 'input',
        'name': 'args',
        'message': 'Enter nmap command',
        #'validate': Ip_Validator,
        'default': '-Sn -P22-243',
    }
]

def screen1():
    global console
    console = Console()
    console.print("""
        .o88o.                               o8o                .
        888 `"                               `"'              .o8
       o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
        888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
        888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
        888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
       o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                    .o...P' """, style="bold red")
def screen2():
    global h
    h = dict()
    h_in = prompt(INPUT_HOST)
    h = h_in.copy()
    for v in h.values():
        h = v
        return h

def screen3():
    global m
    m = dict()
    m_in = prompt(MODE)
    for v in m_in.values():
        m = v
        return m
def screen4():
    started_IA = False
    if 'IA' in m:
        console.print('Starting IA...')
        started_IA = True
    elif 'ROOTS' in m:
        screen5()
def screen5():
    global a
    a = dict()
    a_in = prompt(INPUT_ARGS)
    for v in a.values():
        a = v
        console.print(a)

def debug_screen():
    console.print('Host :',h, style='bold green')
    console.print(type(h), style='bold red')
    console.print('Mode :',m,style='bold green')
    console.print(type(m),style='bold red')
    console.print('Args :',a,style='bold green')
    console.print(type(a),style='bold red')

def main():
    #RUN
    try :
        screen1()
        screen2()
        screen3()
        screen4()
    except:
        debug_screen()
if __name__ == '__main__':
    main()
