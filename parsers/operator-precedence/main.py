# Grammar
#
# program -> expression
#
# expression -> operation
#
# operation -> atom {binary_operator atom}
#
# atom -> literal
# atom -> LEFT_PAREN expression RIGHT_PAREN
# atom -> unary_operator atom
#
# literal -> NUMBER
# literal -> IDENTIFIER
#
# binary_operator -> ADD
# binary_operator -> SUBTRACT
# binary_operator -> MULTIPLY
# binary_operator -> DIVIDE
# binary_operator -> POWER
# binary_operator -> ASSIGN
#
# unary_operator -> SUBTRACT


IDENTIFIER = "IDENTIFIER"
NUMBER = "NUMBER"
LEFT_PAREN = "LEFT_PAREN"
RIGHT_PAREN = "RIGHT_PAREN"
ADD = "ADD"
SUBTRACT = "SUBTRACT"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
POWER = "POWER"
ASSIGN = "ASSIGN"


class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}({self.value})"


class ParseError(Exception):
    def __init__(self, message):
        self.message = message


#########################
######### LEXER #########
#########################


digits = "0123456789"
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def lex(source):
    tokens = []
    while len(source) > 0:
        peek = source[0]

        # Skip whitespace
        if peek == " ":
            _, source = pop(source)
            continue

        # Find operator
        elif peek == "+":
            _, source = pop(source)
            tokens.append(Token(ADD, None))
        elif peek == "-":
            _, source = pop(source)
            tokens.append(Token(SUBTRACT, None))
        elif peek == "*":
            _, source = pop(source)
            tokens.append(Token(MULTIPLY, None))
        elif peek == "/":
            _, source = pop(source)
            tokens.append(Token(DIVIDE, None))
        elif peek == "^":
            _, source = pop(source)
            tokens.append(Token(POWER, None))
        elif peek == "(":
            _, source = pop(source)
            tokens.append(Token(LEFT_PAREN, None))
        elif peek == ")":
            _, source = pop(source)
            tokens.append(Token(RIGHT_PAREN, None))
        elif peek == "=":
            _, source = pop(source)
            tokens.append(Token(ASSIGN, None))

        # Find number
        elif peek in digits:
            value = ""

            while peek in digits:
                next, source = pop(source)
                value += next

                if len(source) == 0:
                    peek = " "
                    break
                peek = source[0]

            tokens.append(Token(NUMBER, value))

        # Find identifier
        elif peek in alpha or peek == "_":
            value = ""

            while peek in alpha or peek in digits or peek == "_":
                next, source = pop(source)
                value += next

                if len(source) == 0:
                    break
                peek = source[0]

            tokens.append(Token(IDENTIFIER, value))

        else:
            next, source = pop(source)
            raise ParseError(f"Unexpected: '{next}'")

    return tokens


##########################
######### PARSER #########
##########################


class OperatorInfo:
    def __init__(self, precendence, associativity):
        self.precedence = precendence
        self.associativity = associativity


LEFT = "LEFT"
RIGHT = "RIGHT"
OPERATOR_INFO = {
    ASSIGN: OperatorInfo(1, RIGHT),
    ADD: OperatorInfo(2, LEFT),
    SUBTRACT: OperatorInfo(2, LEFT),
    MULTIPLY: OperatorInfo(3, LEFT),
    DIVIDE: OperatorInfo(3, LEFT),
    POWER: OperatorInfo(4, RIGHT),
}


def parse(tokens):
    value, _ = operation(tokens)
    return value


def expression(tokens):
    return operation(tokens)


def operation(tokens, min_precedence=1):
    left_value, tokens = atom(tokens)

    while len(tokens) > 0:
        peek = tokens[0]

        operator_info = None
        try:
            operator_info = OPERATOR_INFO[peek.name]
        except:
            break

        if operator_info.precedence < min_precedence:
            break

        new_min_precedence = operator_info.precedence
        if operator_info.associativity == LEFT:
            new_min_precedence += 1

        next, tokens = pop(tokens)
        right_value, tokens = operation(tokens, new_min_precedence)
        left_value = [left_value, next.name, right_value]

    return left_value, tokens


def atom(tokens):
    if len(tokens) == 0:
        raise ParseError("Unexpected end of source")

    peek = tokens[0]

    # Find expression
    if peek.name == LEFT_PAREN:
        _, tokens = pop(tokens)
        value, tokens = operation(tokens)
        next, tokens = pop(tokens)
        if next.name != RIGHT_PAREN:
            raise ParseError("Expected ')'")
        return value, tokens

    # Find literal
    else:
        return pop(tokens)


###########################
######### UTILITY #########
###########################


def pop(iter):
    return iter[0], iter[1:]


while True:
    source = input("> ")
    tokens = lex(source)
    ast = parse(tokens)
    print(ast)
