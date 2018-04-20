##### Lexer for Exp0

from ply import lex

# variables that we need to define for the lexical analysis

tokens = ['NEWLINE'] # we have to define at least one token!

literals = [
    ';',
    'p',
    's',
    '+',
    '-',
    '(',
    ')',
    'x',
    'y',
    'z',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n'
    pass
    
def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex(debug=0)
