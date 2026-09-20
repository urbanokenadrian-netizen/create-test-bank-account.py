from stack_array import ArrayStack

# Higher number binds tighter
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

# 2 ^ 3 ^ 2 means 2 ^ (3 ^ 2), not (2 ^ 3) ^ 2
RIGHT_ASSOCIATIVE = {"^"}


def tokenize(expression):
    """Split expression into whitespace-separated tokens."""
    return expression.split()


def infix_to_postfix(expression, trace=None):
    output = []
    operators = ArrayStack()

    for token in tokenize(expression):
        if token in PRECEDENCE:
            # Pop while higher precedence, or equal & left-associative
            while (not operators.is_empty()
                   and operators.peek() != "("
                   and (PRECEDENCE[operators.peek()] > PRECEDENCE[token]
                        or (PRECEDENCE[operators.peek()] == PRECEDENCE[token]
                            and token not in RIGHT_ASSOCIATIVE))):
                output.append(operators.pop())
            operators.push(token)

        elif token == "(":
            operators.push(token)

        elif token == ")":
            # Drain until we find matching '('
            while not operators.is_empty() and operators.peek() != "(":
                output.append(operators.pop())
            if operators.is_empty():
                raise ValueError("unbalanced parentheses: no matching '('")
            operators.pop()  # Discard the '(' — don't send to output

        else:
            # Number/operand: send straight to output
            output.append(token)

        # Optional trace logging
        if trace is not None:
            trace.append((token, "stack: " + str(operators._items), "output: " + " ".join(output)))

    # After all tokens: pop remaining operators
    while not operators.is_empty():
        op = operators.pop()
        if op == "(":
            raise ValueError("unbalanced parentheses: extra '('")
        output.append(op)

    return " ".join(output)


def apply_operator(operator, left, right):
    """Apply a single operator to two values."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division by zero")
        return left / right
    if operator == "%":
        if right == 0:
            raise ZeroDivisionError("modulo by zero")
        return left % right
    if operator == "^":
        return left ** right
    raise ValueError(f"unknown operator '{operator}'")


def evaluate_postfix(expression, trace=None):
    """Evaluate a postfix (Reverse Polish Notation) expression."""
    values = ArrayStack()

    for token in tokenize(expression):
        if token in PRECEDENCE:
            if values.size() < 2:
                raise ValueError(f"not enough operands for '{token}'")
            right = values.pop()
            left = values.pop()
            result = apply_operator(token, left, right)
            values.push(result)
        else:
            # Convert token to float and push
            values.push(float(token))

        # Optional trace logging
        if trace is not None:
            trace.append((token, "stack: " + str(values._items)))

    if values.size() != 1:
        raise ValueError("malformed expression: wrong number of operands")
    return values.pop()


def convert_and_evaluate(expression):
    """Convert infix → postfix then evaluate; returns (postfix_string, value)."""
    postfix = infix_to_postfix(expression)
    value = evaluate_postfix(postfix)
    return postfix, value


if __name__ == "__main__":
    try:
        postfix, value = convert_and_evaluate("3 + 4 * 2")
        print("infix   : 3 + 4 * 2")
        print("postfix :", postfix)       # Expected: 3 4 2 * +
        print("value   :", value)         # Expected: 11.0
    except Exception as e:
        print("Error:", e)
