# Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# - Expresión no balanceada: { a * ( c + d ) ] - 5 }

import re

def check_parentheses(s):
    punct_marks = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []
    formatted_s = re.sub("[^()\{\}\[\]]", "", s)
    for c in formatted_s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            try:
                if stack[-1] != punct_marks[c]:
                    return False
                else:
                    stack.pop(-1)
            except:
                return False

    if len(stack) > 0:
        return False

    return True

print(check_parentheses("{ [ a * ( c + d ) ] - 5 }")) # True
print(check_parentheses("{ a * ( c + d ) ] - 5 }")) # False
print(check_parentheses("{a + b [c] * (2x2)}}}}")) # False
print(check_parentheses("{a^4 + (((ax4)}")) # False
print(check_parentheses("{{{{{{{}}}}}}}")) # True
print(check_parentheses("(a")) # False
