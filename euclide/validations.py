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
    elif len(symbol) >= 3:
        raise Exception(
            "A Segment must be represented by 2 capital letters or 1 lower letter")

    return True
