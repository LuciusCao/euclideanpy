def symbol_validation(symbol):
    if not isinstance(symbol, str):
        raise Exception("symbol of element must be string")

    return True


def point_validation(symbol):
    _ = symbol_validation(symbol)
    if (len(symbol) != 1) or (not symbol.isalpha()):
        raise Exception("A Point must be represented by a single letter")

    return True


def segment_validation(symbol):
    _ = symbol_validation(symbol)
    if not symbol.isalpha():
        raise Exception("A Segment must be represented by letters")
    if len(symbol) >= 3:
        raise Exception(
            "A Segment must be represented by 2 uppercase letters or 1 lowercase letter")

    return True


def angle_validation(symbol):
    _ = symbol_validation(symbol)
    if (len(symbol) == 3) and (symbol.isalpha()):
        return True
    elif (len(symbol) == 1) and(symbol.isalpha()):
        return True
    elif (len(symbol) == 1) and (symbol.isnumeric()):
        return True
    else:
        raise Exception(
            "An angle must be represented by 1 or 3 letters or 1 digits")

    return False
