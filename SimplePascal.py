from lexer import lexer
from parser import parser

source = 'begin write "a"; end'

result = parser.parse(source, lexer=lexer)
print(result)