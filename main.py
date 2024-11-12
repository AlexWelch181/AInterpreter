import sys

varDict = dict()


def andFunc(s, i):
    return evaluate(s[:i]) and evaluate(s[i + 1:])


def orFunc(s, i):
    return evaluate(s[:i]) or evaluate(s[i + 1:])


def eqFunc(s, i):
    return evaluate(s[:i]) == evaluate(s[i + 1:])


def evaluate(expression):
    operators = {'&': andFunc,
                 '|': orFunc,
                 '=': eqFunc,
                 '!': lambda a, i: not a}
    expression = expression.strip('\n').strip()
    if expression == 'TRUE':
        return True
    elif expression == 'FALSE':
        return False
    if expression is None:
        return None
    if expression in varDict:
        return varDict[expression]
    for operator in operators:
        for index, char in enumerate(expression):
            if char == operator:
                return operators[operator](expression, index)
    return expression


def allocateVar(*args):
    variable_name, expression = args[0].split(':=')
    varDict[variable_name.strip()] = evaluate(expression)


def pogPrint(*args):
    print(evaluate(args[0]))


keywords = {'LET': allocateVar, 'PRINT': pogPrint}


def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            keyword, *linedata = line.split(' ')
            if keyword not in keywords:
                print('Keyword error')
                return
            func = keywords[keyword]
            func(' '.join(linedata))


if __name__ == '__main__':
    main(sys.argv[1])
