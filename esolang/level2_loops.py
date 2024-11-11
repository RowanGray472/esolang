import lark
import esolang.level1_statements

grammar = esolang.level1_statements.grammar + r"""
    %extend start: forloop | whileloop

    forloop: "for" NAME "in" range block
    whileloop: "while" while_condition block
    range: "range" "(" start ")"
    while_condition: start comparison_operator start

    comparison_operator: ">" | "<" | ">=" | "<=" | "==" | "!="
"""
parser = lark.Lark(grammar)


class Interpreter(esolang.level1_statements.Interpreter):
    '''
    >>> interpreter = Interpreter()
    >>> interpreter.visit(parser.parse("for i in range(10) {i}"))
    9
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; a"))
    45
    >>> interpreter.visit(parser.parse("a=0; for i in range(10) {a = a + i}; i")) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: Variable i undefined
    >>> interpreter.visit(parser.parse("a=5; for i in range(a) {a = a + i}; a"))
    15
    >>> interpreter.visit(parser.parse("a=0; while a < 10 {a = a + 1}"))
    10
    >>> interpreter.visit(parser.parse("a=0; wh